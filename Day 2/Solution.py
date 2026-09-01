import pandas as pd
import numpy as np
import time

# ==============================================================================
# 1. DATASET CREATION (Simulating a realistic large e-commerce transaction dataset)
# ==============================================================================
np.random.seed(42)
n_records = 50000  # 50,000 orders to clearly demonstrate benchmark difference

products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]
prices = {"Laptop": 60000, "Smartphone": 25000, "Tablet": 18000, "Headphones": 3000, "Smartwatch": 5000}
regions = ["North", "South", "East", "West", "Central"]
statuses = ["Completed", "Cancelled", "Returned"]
status_weights = [0.80, 0.12, 0.08]  # 80% completed, 12% cancelled, 8% returned

prod_choices = np.random.choice(products, size=n_records)
quantities = np.random.randint(1, 4, size=n_records)
unit_prices = np.array([prices[p] for p in prod_choices])

df = pd.DataFrame({
    "order_id": np.arange(1001, 1001 + n_records),
    "customer_id": [f"CUST_{np.random.randint(1, 500):04d}" for _ in range(n_records)],
    "product": prod_choices,
    "unit_price": unit_prices,
    "quantity": quantities,
    "region": np.random.choice(regions, size=n_records),
    "status": np.random.choice(statuses, size=n_records, p=status_weights),
    "order_date": pd.date_range(start="2026-01-01", periods=n_records, freq="2min")
})


# ==============================================================================
# 2. BENCHMARK: ROW-WISE vs VECTORIZED PROCESSING
# ==============================================================================

# --- Method A: Row-wise Iteration (Iterrows) ---
start_row = time.time()
row_revenue = []
for _, row in df.iterrows():
    if row["status"] == "Completed":
        row_revenue.append(row["quantity"] * row["unit_price"])
    else:
        row_revenue.append(0)
row_time = time.time() - start_row


# --- Method B: Vectorized Operations (NumPy / Pandas Vectorization) ---
start_vec = time.time()
df["revenue"] = np.where(
    df["status"] == "Completed",
    df["quantity"] * df["unit_price"],
    0
)
vector_time = time.time() - start_vec


# ==============================================================================
# 3. ANALYTICS CALCULATIONS
# ==============================================================================

total_revenue = df["revenue"].sum()
revenue_by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)

# Average Order Value (for completed orders)
completed_orders = df[df["status"] == "Completed"]
average_order_value = completed_orders["revenue"].mean()

# Customer Lifetime Value (CLV) & Top Customers
customer_clv = df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False)
top_5_customers = customer_clv.head(5)

# Monthly Revenue Trend
monthly_revenue = df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum()

# Cancellation & Return Percentages
total_orders = len(df)
cancelled_pct = (df["status"] == "Cancelled").mean() * 100
returned_pct = (df["status"] == "Returned").mean() * 100


# ==============================================================================
# 4. DISPLAY RESULTS
# ==============================================================================

print("=" * 70)
print("             E-COMMERCE ORDER ANALYTICS ENGINE REPORT")
print("=" * 70)
print(f"Total Processed Transactions : {total_orders:,}")
print(f"Total Revenue Generated      : ₹{total_revenue:,.2f}")
print(f"Average Order Value (AOV)    : ₹{average_order_value:,.2f}")
print(f"Cancelled Orders Rate        : {cancelled_pct:.2f}%")
print(f"Returned Orders Rate         : {returned_pct:.2f}%")

print("\n--- Revenue by Product Category ---")
for prod, rev in revenue_by_product.items():
    print(f"  • {prod:<15} : ₹{rev:>14,.2f}")

print("\n--- Revenue by Region ---")
for reg, rev in revenue_by_region.items():
    print(f"  • {reg:<15} : ₹{rev:>14,.2f}")

print("\n--- Top 5 Most Valuable Customers (CLV) ---")
for cust, clv in top_5_customers.items():
    print(f"  • Customer {cust} : ₹{clv:>12,.2f}")

print("\n--- Monthly Revenue ---")
for month, rev in monthly_revenue.items():
    print(f"  • {str(month):<10} : ₹{rev:>14,.2f}")

print("\n" + "=" * 70)
print("            PERFORMANCE BENCHMARK (Row-Wise vs Vectorized)")
print("=" * 70)
print(f"Row-wise processing time  : {row_time:.4f} seconds")
print(f"Vectorized processing time: {vector_time:.4f} seconds")
speedup = row_time / vector_time if vector_time > 0 else 0
print(f"Vectorization Speedup     : ~{speedup:.1f}x FASTER 🚀")
print("=" * 70)
