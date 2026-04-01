import streamlit as st
import pandas as pd

from agents.finance_agent import check_invoice_vs_po
from agents.monitoring_agent import monitor_integrations
from agents.ai_assistant import ask_copilot

# Page title
st.title("Ford Tax Systems AI Copilot")

st.write("Enterprise tax monitoring and finance governance dashboard")

# -----------------------------
# TRANSACTION MONITORING
# -----------------------------

st.header("Transaction Monitoring")

transactions = pd.read_csv("data/transactions.csv")

st.dataframe(transactions)

st.bar_chart(transactions["amount"])

# -----------------------------
# INVOICE VALIDATION
# -----------------------------

st.header("Invoice vs Purchase Order Validation")

if st.button("Check Invoice Issues"):

    issues = check_invoice_vs_po()

    if len(issues) == 0:
        st.success("No invoice issues detected")
    else:
        st.error("Invoice issues detected")
        st.dataframe(issues)

# -----------------------------
# INTEGRATION MONITORING
# -----------------------------

st.header("Integration Monitoring")

if st.button("Check System Interfaces"):

    failures = monitor_integrations()

    if len(failures) == 0:
        st.success("All integrations working normally")
    else:
        st.error("Integration issues detected")
        st.write(failures)

# -----------------------------
# AI TAX COPILOT
# -----------------------------

st.header("AI Tax Systems Copilot")

question = st.text_input("Ask a question about tax systems")

if question:

    answer = ask_copilot(question)

    st.write("AI Copilot:", answer)