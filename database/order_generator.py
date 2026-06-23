import psycopg2
from psycopg2.extras import execute_values
import random
from faker import Faker

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()

statuses = [
    "Pending",
    "Delivered",
    "Cancelled",
    "Shipped"
]

batch_size = 10000
total_orders = 1000000

print("Generating 1 million orders...")

for batch in range(total_orders // batch_size):

    orders = []

    for _ in range(batch_size):
        orders.append(
            (
                random.randint(1, 110000),
                round(random.uniform(100, 10000), 2),
                random.choice(statuses),
                fake.date_time_this_decade()
            )
        )

    execute_values(
        cursor,
        """
        INSERT INTO orders(
            customer_id,
            amount,
            status,
            order_date
        )
        VALUES %s
        """,
        orders
    )

    conn.commit()

    print(f"Inserted {(batch+1)*batch_size} orders")

cursor.close()
conn.close()

print("1 million orders inserted successfully!")