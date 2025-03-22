import pandas as pd


df = pd.read_csv("dataset.csv")

# 1. Calculate total revenue
df["revenue"] = df["price"] * df["quantity_sold"]
total_revenue = df["revenue"].sum()
print(f"Total Revenue: ${total_revenue:.2f}")

# 2. Find category with highest revenue
category_revenue = df.groupby("category")["revenue"].sum()
highest_revenue_category = category_revenue.idxmax()
print(f"Category with Highest Revenue: {highest_revenue_category} (${category_revenue.max():.2f})")

# 3. Find the most sold product
most_sold_product = df.loc[df["quantity_sold"].idxmax(), "product"]
print(f"Most Sold Product: {most_sold_product} ({df['quantity_sold'].max()} units)")