"""
SCRIPT: seed_data.py
GOAL: Generates synthetic supply chain data for SQL training
"""

import sqlite3
import random
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

# --- Configuration ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent # BACK 2 da root
DB_PATH = BASE_DIR / "logistik_playground.db"
SCHEMA_PATH = Path(__file__).resolve().parent /"schema_setup.sql"

def init_db():
    """Reads the SQL schema and builds empty tables."""
    print(f"Initializing database: {DB_PATH.name}...")
   
   # Read SQL file (Clean code style)
sql_script = SCHEMA_PATH.read_text(encoding='utf-8')

with sqlite3.connect(DB_PATH) as conn:
    conn.executescript(sql_script)
    print("Database initialized successfully.")

def generate_products(N=20):
    """Generates N synthetic products with random attributes."""
    categories = ['Electronics', 'Automotive', 'Office', 'Home']
    products = []

    for i in range(1, N+1):
        prod = {
            'product_id': i,
            'sku': f'SKU-{random.randint(1000, 9999)}-X',
            'name': f'Item_type_{i}',
            'category': random.choice(categories),
            'price_eur': round(random.uniform(5.0, 500.0), 2)
        }
        products.append(prod)
    return pd.DataFrame(products)

def generate_movements(product_ids, N=100):
    """Generates N synthetic inventory movements for products."""   
    movements = []
    zones = ['A-01', 'B-05', 'C-10', 'D-Dock']

    for i in range(N):
        #Generate random date within the last 30 days
        random_days = random.randint(0, 30)
        date =datetime.now() - timedelta(days=random_days)

        movements.append({
            'product_id': random.choice(product_ids),
            'movement_type': random.choice(['INBOUND', 'OUTBOUND', 'RETURN']),
            'quantity': random.randint(1, 50),
            'movement_date': date.strftime('%Y-%m-%d %H:%M:%S'),
            'warehouse_zone': random.choice(zones)
        })
    return pd.DataFrame(movements)

def main():
        # 1. Build structure
        init_db()

        #2. Generate data (Python Logic)
        print('Generating synthetic data...')
        df_products = generate_products(N=50)

        #create a list of IDs for movements to reference
        product_ids = df_products['product_id'].tolist()
        df_movements = generate_movements(product_ids, N=200)

        #3. Load to DB (Pandas power)
        with sqlite3.connect(DB_PATH) as conn:
            #if_exists='append' ensures data is added without overwriting
            df_products.to_sql('products', conn, if_exists='append', index=False)
            df_movements.to_sql('inventory_movements', conn, if_exists='append', index=False)

            print(f" Inserted {len(df_products)} products and {len(df_movements)} movements into the database.")

if __name__ == '__main__':
    main()
    