import json
import os
from .metrics import METRICS


def choose_metric(question: str) -> str | None:
    question_lower = question.lower().strip()
    if not question_lower:
        return None

    # Safe deterministic routing works without an API key.
    matches = [m.name for m in METRICS.values() if any(a in question_lower for a in m.aliases)]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        return None

    if not os.getenv("OPENAI_API_KEY"):
        return None

    # LLM is a classifier, never a SQL author or database query executor.
    from openai import OpenAI
    choices = [{"name": m.name, "description": m.description} for m in METRICS.values()]
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=("Select exactly one approved KPI from the available names if the user's "
                      "question clearly requests it. Otherwise choose 'unsupported'. "
                      "Never invent a metric, value, or SQL query."),
        input=json.dumps({"question": question, "allowed_metrics": choices}),
        text={"format": {"type": "json_schema", "name": "metric_selection", "strict": True,
                         "schema": {"type": "object", "properties": {
                             "metric": {"type": "string", "enum": [*METRICS.keys(), "unsupported"]}},
                             "required": ["metric"], "additionalProperties": False}}},
    )
    selected = json.loads(response.output_text)["metric"]
    return selected if selected in METRICS else None
