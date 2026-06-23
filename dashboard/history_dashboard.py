import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(
    page_title="Optimization History",
    layout="wide"
)

st.title("📜 Optimization History Dashboard")

# -------------------
# Database Connection
# -------------------

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",
    port="5432"
)

query = """
SELECT
problem,
recommendation,
before_time,
after_time,
improvement,
created_at
FROM optimization_history
ORDER BY created_at DESC;
"""

df = pd.read_sql(query, conn)

st.subheader("Previous Optimizations")

st.dataframe(df)

conn.close()