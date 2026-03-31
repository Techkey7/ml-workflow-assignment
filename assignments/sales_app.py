

import streamlit as st
import pandas as pd

# -------------------------------
# Title & Description
# -------------------------------
st.title("Sales Summary Dashboard")
st.subheader("Filter sales data by category")

# -------------------------------
# Hardcoded Dataset
# -------------------------------
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Camera"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Sales": [10000, 20000, 16000, 3000, 12000]
}

df = pd.DataFrame(data)

# -------------------------------
# Sidebar Filter
# -------------------------------
st.sidebar.header("Filter Options")

category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

# -------------------------------
# Filter Data
# -------------------------------
filtered_df = df[df["Category"] == category]

# -------------------------------
# Display Table
# -------------------------------
st.write("Filtered Data")
st.dataframe(filtered_df)

# -------------------------------
# Line Chart
# -------------------------------
st.write("Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])