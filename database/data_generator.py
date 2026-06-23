import psycopg2
from faker import Faker
import random

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",      # replace if your password is different
    port="5432"
)

cursor = conn.cursor()

print("Connected to database...")

# Generate customers
customers = []

for i in range(100000):
    customers.append(
        (
            fake.name(),
            fake.city(),
            fake.email()
        )
    )

cursor.executemany(
    """
    INSERT INTO customers(name, city, email)
    VALUES (%s,%s,%s)
    """,
    customers
)

conn.commit()

print("10,000 customers inserted!")

cursor.close()
conn.close()