import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------
# Page Configuration
# ----------------------

st.set_page_config(
    page_title="Self-Healing PostgreSQL Optimizer",
    layout="wide"
)

st.title("🚀 Self-Healing PostgreSQL Optimization Engine")

# ----------------------
# Load JSON Report
# ----------------------

with open("optimization_report.json") as file:
    report = json.load(file)

problem = report["problem"]
index_added = report["index_added"]
before_time = report["before_time"]
after_time = report["after_time"]
improvement = report["improvement_percent"]

# ----------------------
# Metrics
# ----------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Before Time",
    f"{before_time} ms"
)

col2.metric(
    "After Time",
    f"{after_time} ms"
)

col3.metric(
    "Improvement",
    f"{improvement}%"
)

col4.metric(
    "Index Added",
    index_added
)

st.divider()

# ----------------------
# Problem Information
# ----------------------

st.subheader("Problem Information")

st.success(problem)

st.write("Index Added :", index_added)

st.write("Improvement :", improvement, "%")

# ----------------------
# Bar Chart
# ----------------------

st.subheader("Before vs After")

df = pd.DataFrame(
    {
        "Stage": ["Before", "After"],
        "Execution Time": [before_time, after_time]
    }
)

fig, ax = plt.subplots()

ax.bar(
    df["Stage"],
    df["Execution Time"]
)

ax.set_ylabel("Execution Time (ms)")

st.pyplot(fig)


# ----------------------
# Report Table
# ----------------------

st.subheader("Optimization Report")

st.dataframe(df)