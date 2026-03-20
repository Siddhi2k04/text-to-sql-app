import sqlite3

conn = sqlite3.connect("database/db.sqlite")
cursor = conn.cursor()

# 🔥 Drop tables (reset)
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS orders")

# 🔥 Create tables
cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    date TEXT
)
""")

# 🔥 Insert customers
customers_data = [
    (1, "Amit", "Mumbai"),
    (2, "Priya", "Pune"),
    (3, "Rahul", "Delhi"),
    (4, "Sneha", "Mumbai"),
    (5, "Arjun", "Bangalore"),
    (6, "Neha", "Pune"),
    (7, "Karan", "Delhi"),
    (8, "Pooja", "Mumbai"),
    (9, "Rohan", "Chennai"),
    (10, "Anjali", "Kolkata")
]

cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers_data)

# 🔥 Insert orders
orders_data = [
    (1, 1, 2500, "2024-01-01"),
    (2, 2, 6000, "2024-01-05"),
    (3, 1, 4500, "2024-01-10"),
    (4, 3, 8000, "2024-01-12"),
    (5, 4, 3000, "2024-01-15"),
    (6, 5, 10000, "2024-01-18"),
    (7, 2, 2000, "2024-01-20"),
    (8, 6, 7000, "2024-01-22"),
    (9, 7, 1500, "2024-01-25"),
    (10, 8, 9000, "2024-01-28"),
    (11, 1, 5200, "2024-02-01"),
    (12, 3, 4300, "2024-02-05"),
    (13, 4, 7600, "2024-02-08"),
    (14, 6, 3100, "2024-02-12"),
    (15, 9, 8800, "2024-02-15")
]

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders_data)

conn.commit()
conn.close()

print("✅ Database initialized!")