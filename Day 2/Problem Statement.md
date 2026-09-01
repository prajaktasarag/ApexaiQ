# Problem 5 — E-Commerce Order Analytics Engine

## Problem Statement

Given a large dataset of e-commerce transactions, build an analytics engine that calculates:

- Total revenue
- Revenue by product
- Revenue by region
- Average order value
- Customer lifetime value
- Top customers
- Monthly revenue
- Cancelled-order percentage
- Return percentage

The solution should be optimized for large datasets.

The program should also compare:

- Row-wise processing
- Vectorized processing

and explain the performance difference between them.

---

## Solution

The solution uses **Python and Pandas** to analyze e-commerce transaction data.

The dataset contains information such as:

- Order ID
- Customer ID
- Product
- Region
- Order Date
- Quantity
- Price
- Order Status
- Return Status

### Processing Flow

```text
Transaction Dataset
        ↓
    Load Data
        ↓
   Calculate Revenue
        ↓
     Analytics
        ↓
Row-wise vs Vectorized
        ↓
   Benchmark Results
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Time module

---

## Analytics Performed

### 1. Total Revenue

Calculates the total revenue generated from completed orders.

```text
Revenue = Quantity × Price
```

### 2. Revenue by Product

Calculates how much revenue each product generated.

### 3. Revenue by Region

Calculates revenue generated from each region.

### 4. Average Order Value

Calculates the average amount spent per order.

```text
Average Order Value = Total Revenue / Number of Orders
```

### 5. Customer Lifetime Value

Calculates the total amount spent by each customer.

### 6. Top Customers

Finds customers who generated the highest revenue.

### 7. Monthly Revenue

Groups revenue according to month to understand monthly sales performance.

### 8. Cancelled Order Percentage

Calculates the percentage of orders that were cancelled.

### 9. Return Percentage

Calculates the percentage of orders that were returned.

---

## Row-wise vs Vectorized Processing

### Row-wise Processing

Row-wise processing checks each row individually using a loop.

```text
Row 1 → Calculate
Row 2 → Calculate
Row 3 → Calculate
...
```

This approach is easy to understand but slower for large datasets.

### Vectorized Processing

Vectorized processing performs operations on entire Pandas columns at once.

Example:

```python
df["revenue"] = df["quantity"] * df["price"]
```

Instead of processing every row separately, Pandas performs the operation on the complete column.

This is generally much faster for large datasets.

---

## Benchmark

The program measures the execution time of both approaches.

```text
Row-wise Time   : X.XXXX seconds
Vectorized Time : X.XXXX seconds
```

The results are used to compare their performance.

### Expected Result

Vectorized operations are generally faster because Pandas performs many operations internally using optimized numerical routines instead of executing Python-level loops for every row.

---

## Conclusion

The E-Commerce Order Analytics Engine calculates important business statistics such as revenue, customer value, product performance, regional performance, monthly revenue, cancellations, and returns.

The comparison shows that **vectorized Pandas operations are generally more efficient than row-wise processing**, especially when working with large datasets.

---

## Source Code

📄 **Python Implementation:**

[View Solution.py](Solution.py)
