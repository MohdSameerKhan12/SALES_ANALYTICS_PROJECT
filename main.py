import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

# CSV Load
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "data" / "sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = pd.to_datetime(df["Date"])
# KPIs
df["Revenue"] = df["Quantity" ] * df["Price"]
total_revenue = df["Revenue"].sum()
total_orders = len(df)
top_city = df.groupby("City")["Revenue"].sum().idxmax()

st.title("📊 Sales Analytics Dashboard")
# City Filter
date = st.sidebar.date_input(
    "Select Date",
    value=None
)
if date:
    df = df[df["Date"].dt.date == date]
search = st.sidebar.text_input("🔍 Search Product")

if search:
    df = df[df["Product"].str.contains(search, case=False, na=False)]

product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + list(df["Product"].unique())
)

if product != "All":
    df = df[df["Product"] == product]

city = st.sidebar.selectbox(
    "Select City",
    ["All"] + list(df["City"].unique())
)

if city != "All":
    df = df[df["City"] == city]
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Revenue", f"₹{total_revenue:,}")

with col2:
    st.metric("Total Orders", total_orders)

with col3:
    st.metric("Top City", top_city)

st.write("### Sales Data")
st.dataframe(df)
st.download_button(
    label="📥 Download Filtered Data",
    data=df.to_csv(index=False),
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)
st.subheader("Revenue by City")

city_sales = df.groupby("City")["Revenue"].sum()

st.bar_chart(city_sales)
st.subheader("Category-wise Revenue")

category_sales = df.groupby("Category")["Revenue"].sum()

st.bar_chart(category_sales)
st.subheader("Top 5 Products by Revenue")

product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

st.bar_chart(product_sales.head(5))
st.subheader("Download Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Sales Data",
    data=csv,
    file_name="sales_data.csv",
    mime="text/csv"
)
st.subheader("📈 Daily Revenue Trend")
daily_revenue = df.groupby("Date")["Revenue"].sum().reset_index()

fig = px.line(
    daily_revenue,
    x="Date",
    y="Revenue",
    title="Daily Revenue Trend",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)
daily_revenue = df.groupby("Date")["Revenue"].sum()
st.subheader("Category-wise Revenue")

category_sales = df.groupby("Category")["Revenue"].sum()

fig, ax = plt.subplots(figsize=(6,6))
ax.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.axis("equal")

st.pyplot(fig)
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(daily_revenue.index, daily_revenue.values, marker="o")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue")
ax.set_title("Daily Revenue")
plt.xticks(rotation=45)

st.pyplot(fig)
st.subheader("📊 Product-wise Sales")

product_sales = df.groupby("Product")["Quantity"].sum()

fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.bar(product_sales.index, product_sales.values)
ax2.set_xlabel("Product")
ax2.set_ylabel("Quantity Sold")
ax2.set_title("Top Selling Products")
plt.xticks(rotation=45)

st.pyplot(fig2)
import matplotlib.pyplot as plt

st.subheader("Revenue by City")

city_revenue = df.groupby("City")["Revenue"].sum()

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(city_revenue.index, city_revenue.values)
ax.set_xlabel("City")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by City")

st.pyplot(fig)
st.subheader("🥧 Sales by Category")

category_revenue = df.groupby("Category")["Revenue"].sum()

fig3, ax3 = plt.subplots(figsize=(6,6))
ax3.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%",
    startangle=90
)
ax3.set_title("Revenue by Category")

st.pyplot(fig3)
st.subheader("Category Revenue Summary")

category_summary = (
    df.groupby("Category")["Revenue"]
      .sum()
      .reset_index()
)

st.dataframe(category_summary)
