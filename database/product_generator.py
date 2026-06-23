import psycopg2
from psycopg2.extras import execute_values
import random

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()

categories = [
    "Electronics",
    "Fashion",
    "Books",
    "Sports",
    "Home",
    "Toys"
]

products = []

for i in range(10000):
    products.append(
        (
            random.choice(categories),
            round(random.uniform(100, 50000), 2)
        )
    )

execute_values(
    cursor,
    """
    INSERT INTO products(category, price)
    VALUES %s
    """,
    products
)

conn.commit()

print("10000 products inserted!")

cursor.close()
conn.close()