import pandas as pd

# Assumption: The dataset is in a CSV file named 'data_penjualan.csv' in the same directory as this script.
# The user provided the content and name of this CSV.
try:
    df = pd.read_csv('data_penjualan.csv')
except FileNotFoundError:
    print("Error: 'data_penjualan.csv' not found. Please ensure the dataset file is in the correct directory.")
    exit()

print("--- Data Exploration ---")
# 2. Display the first 5 rows of the dataset.
print("\nFirst 5 rows of the dataset:")
print(df.head().to_markdown(index=False))

# 2. Display a concise summary of the dataset information.
print("\nConcise summary of the dataset information:")
df.info()

print("\n--- Data Analysis ---")
# 3. Create a new column named Total_Pendapatan which is the result of multiplying Harga_Satuan by Jumlah_Terjual.
df['Total_Pendapatan'] = df['Harga_Satuan'] * df['Jumlah_Terjual']
print("\nDataset with 'Total_Pendapatan' column (first 5 rows):")
print(df.head().to_markdown(index=False))

# 3. Calculate and display the overall total revenue from all transactions.
overall_total_revenue = df['Total_Pendapatan'].sum()
print(f"\nOverall total revenue from all transactions: ${overall_total_revenue:,.2f}")

# 3. Find and display the product with the highest quantity sold.
# Using 'Nama_Produk' for product name and 'Jumlah_Terjual' for quantity sold.
product_quantity = df.groupby('Nama_Produk')['Jumlah_Terjual'].sum()
product_highest_quantity_sold = product_quantity.idxmax()
highest_quantity = product_quantity.max()
print(f"\nProduct with the highest quantity sold: '{product_highest_quantity_sold}' with {highest_quantity} units sold.")

# 3. Calculate the total revenue for each product category.
# Using 'Kategori' for product category as per the provided CSV.
revenue_per_category = df.groupby('Kategori')['Total_Pendapatan'].sum()
print("\nTotal revenue for each product category:")
print(revenue_per_category.sort_values(ascending=False).to_markdown())

# 3. Filter and display transactions where the quantity sold is greater than 20.
transactions_gt_20 = df[df['Jumlah_Terjual'] > 20]
print("\nTransactions where the quantity sold is greater than 20:")
print(transactions_gt_20.to_markdown(index=False))

print("\n--- Saving Results ---")
# 4. Create a new DataFrame containing the aggregated revenue per category.
df_category_summary = revenue_per_category.reset_index()
df_category_summary.columns = ['Kategori_Produk', 'Total_Pendapatan_Per_Kategori']

# 5. Save this new DataFrame to a CSV file named category_summary.csv. Do not include the row index in the saved CSV file.
df_category_summary.to_csv('category_summary.csv', index=False)
print("Aggregated revenue per category saved to 'category_summary.csv'")

print("\nPython script execution complete. Please check 'category_summary.csv' for the saved data.")
