import sqlite3

def get_connection():
    return sqlite3.connect("database/db.sqlite")

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    conn.close()
    
    return columns, results