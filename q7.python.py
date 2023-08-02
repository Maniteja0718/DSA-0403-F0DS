import pandas as pd

order_data = {
    'customer_id': [2, 3, 4],
    'order_date': ['1-08-2023', '1-08-2023', '2-08-2023'],
    'product_name': ['shoes', 'shirt', 'watch'],
    'order_quantity': [100, 200, 20]
}

df = pd.DataFrame(order_data)
print(df)

orders_per_customer = df.groupby('customer_id')['order_date'].count()
print(orders_per_customer)

avg_order_quantity_per_product = df.groupby('product_name')['order_quantity'].mean()
print(avg_order_quantity_per_product)

earliest_order_date = df['order_date'].min()
latest_order_date = df['order_date'].max()
print("Earliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
