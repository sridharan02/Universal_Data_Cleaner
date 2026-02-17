import pandas as pd

# 1. Load the messy data
df = pd.read_csv("messy_operations_data.csv")

# 2. Clean: Remove rows where the 'ID' is missing
df = df.dropna(subset=['ID'])

# 3. Clean: Fix date formats to YYYY-MM-DD
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

# 4. Logic: Calculate a 'Total Cost' column if it's missing
df['Total_Cost'] = df['Quantity'] * df['Unit_Price']

# 5. Save to SQL (Simplest way)
# df.to_sql('cleaned_tasks', engine, if_exists='append')