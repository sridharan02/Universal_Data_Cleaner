import pandas as pd
import mysql.connector

# 1. SETUP CONNECTION
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="lucky$shot.123", # <--- Put your actual SQL password here
        database="OpsManager"
    )
    cursor = db.cursor()
    print("Successfully connected to the database!")

    # 2. LOAD MESSY DATA
    df = pd.read_csv("daily.csv")
    print("Loaded messy CSV file...")

    # 3. THE CLEANING LOGIC (The main feature)
    # Fix missing quantities: replace empty cells with 0
    df['quantity_used'] = df['quantity_used'].fillna(0)
    
    # Fix Status: make everything lowercase and fill missing with 'unknown'
    df['status'] = df['status'].str.lower().fillna('unknown')

    # 4. UPLOAD TO SQL
    for index, row in df.iterrows():
        query = "INSERT INTO Operations_Log (item_id, quantity_used, status, entry_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (int(row['item_id']), int(row['quantity_used']), row['status'], row['entry_date']))
    
    db.commit()
    print(f"Success! {len(df)} rows cleaned and uploaded.")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()