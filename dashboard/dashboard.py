import streamlit as st
import pandas as pd

transactions = pd.read_csv("data/transactions.csv")

st.title("Ford Tax Systems Dashboard")

st.subheader("Transaction Amounts")

st.bar_chart(transactions["amount"])