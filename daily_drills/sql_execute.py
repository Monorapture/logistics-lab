import sqlite3
from pathlib import Path
import pandas as pd

# Innerhalb der Funktion: Vertraue den Argumenten!
def execute_sql_from_file(database_path, sql_file_path):
    
    # Check if files exist
    if not sql_file_path.exists():
        raise FileNotFoundError(f"SQL file missing: {sql_file_path}")
    
    query = sql_file_path.read_text(encoding='utf-8')
    
    with sqlite3.connect(database_path) as conn:
        conn.execute("DROP VIEW IF EXISTS view_event_log")
       
        conn.executescript(query)
        print("✅ View 'view_event_log' created successfully.")
        
        # Optional: Read the newly created view into a DataFrame
        return pd.read_sql_query("SELECT * FROM view_event_log LIMIT 10", conn)

# --- Usage (Draußen die Pfade bauen) ---
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent # Root
    MY_DB = BASE_DIR / "logistik_playground.db"
    MY_SQL = Path(__file__).resolve().parent / "create_view_eventlog.sql"

    try:
        # Jetzt übergeben wir die Pfad-Objekte
        df = execute_sql_from_file(MY_DB, MY_SQL)
        print(df.head())
    except Exception as e:
        print(f"❌ Error: {e}")