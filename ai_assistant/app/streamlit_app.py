import os
from pathlib import Path
import httpx
import streamlit as st
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000").rstrip("/")
st.set_page_config(page_title="CommerceIQ 360 | AI KPI Assistant", page_icon="📊")
st.title("CommerceIQ 360 — AI KPI Assistant")
st.caption("Answers are sourced from approved PostgreSQL analytics KPIs.")
question = st.chat_input("Ask: How many delivered orders do we have?")
if question:
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        try:
            result = httpx.post(f"{API_URL}/api/v1/ask", json={"question": question}, timeout=15)
            result.raise_for_status()
            payload = result.json()
            st.write(payload["answer"])
            if payload.get("evidence"):
                with st.expander("Verified KPI evidence"):
                    st.json(payload["evidence"])
        except httpx.HTTPError:
            st.error("Cannot reach the KPI backend. Check that Uvicorn is running.")
