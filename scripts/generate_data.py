import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate date range (2 years of data)
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Product categories and products
categories = {
    'Electronics': ['Wireless Headphones', 'Smart Watch', 'Laptop', 'Tablet', 'Bluetooth Speaker'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Sneakers', 'Dress'],
    'Home & Garden': ['Coffee Maker', 'Vacuum Cleaner', 'Bed Sheets', 'Garden Tools', 'Lamp'],
    'Sports': ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Fitness Tracker', 'Bicycle'],
    'Books': ['Fiction Novel', 'Cookbook', 'Self-Help Book', 'Biography', 'Science Book']
}

# Price ranges for each category
price_ranges = {
    'Electronics': (50, 1200),
    'Clothing': (15, 150),
    'Home & Garden': (20, 300),
    'Sports': (25, 500),
    'Books': (10, 40)
}

# Customer demographics
regions = ['North', 'South', 'East', 'West', 'Central']
age_groups = ['18-25', '26-35', '36-45', '46-55', '56+']
genders = ['Male', 'Female', 'Other']

# Generate sales data
sales_data = []
order_id = 1000

for date in dates:
    # Number of orders per day (with seasonal variation)
    month = date.month
    # More sales in Nov-Dec (holiday season) and Jul-Aug (summer)
    if month in [11, 12]:
        daily_orders = random.randint(40, 80)
    elif month in [7, 8]:
        daily_orders = random.randint(35, 65)
    else:
        daily_orders = random.randint(20, 45)
    
    for _ in range(daily_orders):
        # Select category and product
        category = random.choice(list(categories.keys()))
        product = random.choice(categories[category])
        
        # Generate price with some variation
        base_price = random.uniform(*price_ranges[category])
        price = round(base_price, 2)
        
        # Quantity (mostly 1-3, occasionally higher)
        if random.random() < 0.85:
            quantity = random.randint(1, 3)
        else:
            quantity = random.randint(4, 8)
        
        # Calculate total
        total = round(price * quantity, 2)
        
        # Customer information
        customer_id = f"CUST{random.randint(1, 500):04d}"
        region = random.choice(regions)
        age_group = random.choice(age_groups)
        gender = random.choice(genders)
        
        # Payment method
        payment_method = random.choice(['Credit Card', 'PayPal', 'Debit Card', 'Gift Card'])
        
        # Shipping method
        shipping = random.choice(['Standard', 'Express', 'Next Day'])
        
        sales_data.append({
            'Order_ID': f"ORD{order_id}",
            'Date': date.strftime('%Y-%m-%d'),
            'Year': date.year,
            'Month': date.strftime('%B'),
            'Month_Num': date.month,
            'Quarter': f"Q{(date.month-1)//3 + 1}",
            'Day_of_Week': date.strftime('%A'),
            'Category': category,
            'Product': product,
            'Unit_Price': price,
            'Quantity': quantity,
            'Total_Sales': total,
            'Customer_ID': customer_id,
            'Region': region,
            'Age_Group': age_group,
            'Gender': gender,
            'Payment_Method': payment_method,
            'Shipping_Method': shipping
        })
        
        order_id += 1

# Create DataFrame
df = pd.DataFrame(sales_data)

# Save to CSV
df.to_csv('ecommerce_sales_data.csv', index=False)

print(f"Dataset created successfully!")
print(f"Total Orders: {len(df):,}")
print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Total Revenue: ${df['Total_Sales'].sum():,.2f}")
print(f"\nFirst few rows:")
print(df.head(10).to_string())

# Create summary statistics for analysis
print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)

print("\n Sales by Category:")
category_sales = df.groupby('Category')['Total_Sales'].agg(['sum', 'count']).round(2)
category_sales.columns = ['Total_Revenue', 'Orders']
category_sales = category_sales.sort_values('Total_Revenue', ascending=False)
print(category_sales.to_string())

print("\n Sales by Quarter (2024):")
quarterly_2024 = df[df['Year'] == 2024].groupby('Quarter')['Total_Sales'].sum().round(2)
print(quarterly_2024.to_string())

print("\n Top 5 Products by Revenue:")
top_products = df.groupby('Product')['Total_Sales'].sum().round(2).sort_values(ascending=False).head()
print(top_products.to_string())

print("\n Sales by Region:")
region_sales = df.groupby('Region')['Total_Sales'].sum().round(2).sort_values(ascending=False)
print(region_sales.to_string())

print(f"\n File saved as: ecommerce_sales_data.csv")
