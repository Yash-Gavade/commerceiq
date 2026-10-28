import json
import os
import re
from .metrics import METRICS


def choose_metric(question: str) -> str | None:
    normalized = " ".join(re.findall(r"[a-z0-9]+", question.lower()))
    if not normalized:
        return None

    # High-priority intent rules: 'delivered orders' is a population/filter,
    # not the requested metric, when the question explicitly asks for GMV.
    tokens = set(normalized.split())
    delivered = "delivered" in tokens or "delivery" in tokens
    monetary = bool(tokens & {"gmv", "revenue", "merchandise"})
    asks_average = "aov" in tokens or "average order value" in normalized

    if asks_average and delivered:
        return "delivered_aov"
    if asks_average:
        return "delivered_aov" if "delivered_aov" in METRICS else None
    if monetary and delivered:
        return "delivered_gmv" if "delivered_gmv" in METRICS else None
    if "gmv" in tokens and ("total" in tokens or "overall" in tokens):
        return "total_gmv" if "total_gmv" in METRICS else None
    if "how many" in normalized and "delivered" in tokens and "orders" in tokens:
        return "delivered_orders"
    # Longer (more specific) phrases win; conflicting equally specific matches abstain.
    ranked = []
    for metric in METRICS.values():
        lengths = [len(alias.split()) for alias in metric.aliases
                   if " ".join(re.findall(r"[a-z0-9]+", alias.lower())) in normalized
                   and re.search(r"\b" + re.escape(" ".join(re.findall(r"[a-z0-9]+", alias.lower()))) + r"\b", normalized)]
        if lengths:
            ranked.append((max(lengths), metric.name))
    if ranked:
        top = max(score for score, _ in ranked)
        winners = [name for score, name in ranked if score == top]
        return winners[0] if len(winners) == 1 else None

    if not os.getenv("OPENAI_API_KEY"):
        return None

    from openai import OpenAI
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    choices = [{"name": m.name, "description": m.description} for m in METRICS.values()]
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=("Select one metric only if the question unambiguously asks for it, "
                      "else choose 'unsupported'. Do not produce SQL or calculate numbers."),
        input=json.dumps({"question": question, "allowed_metrics": choices}),
        text={"format": {"type": "json_schema", "name": "metric_selection", "strict": True,
                         "schema": {"type": "object", "properties": {
                             "metric": {"type": "string", "enum": [*METRICS.keys(), "unsupported"]}},
                             "required": ["metric"], "additionalProperties": False}}},
    )
    selected = json.loads(response.output_text)["metric"]
    return selected if selected in METRICS else None
