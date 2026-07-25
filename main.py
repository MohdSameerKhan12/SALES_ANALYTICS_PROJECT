import pandas as pd
import matplotlib.pylab as plt
# Data load
df = pd.read_csv("data/sales_data.csv")

# Total Sales column banao
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Total Revenue
print("Total Revenue:", df["Total_Sales"].sum())

# Top Selling Product
print("\nTop Selling Products:")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False))

# City Wise Revenue
print("\nCity Wise Revenue:")
print(df.groupby("City")["Total_Sales"].sum())
# Bar Chart - City Wise Revenue
city_revenue = df.groupby("City")["Total_Sales"].sum()

plt.figure(figsize=(6,4))
city_revenue.plot(kind="bar")

plt.title("City Wise Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.grid(True)

plt.show()
# Top Selling Products Chart
top_products = df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(6,4))
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Pie Chart - Revenue Distribution by City

plt.figure(figsize=(6,6))

city_revenue.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue Distribution by City")
plt.ylabel("")
plt.show()
# Daily Sales Trend

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(8,4))
daily_sales.plot(kind="line", marker="o")

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
