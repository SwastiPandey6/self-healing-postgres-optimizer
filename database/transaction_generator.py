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

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash"
]

transactions = []

for _ in range(100000):

    transactions.append(
        (
            random.randint(1, 110000),
            random.choice(payment_modes),
            fake.date_time_this_decade()
        )
    )

execute_values(
    cursor,
    """
    INSERT INTO transactions(
        customer_id,
        payment_mode,
        transaction_time
    )
    VALUES %s
    """,
    transactions
)

conn.commit()

print("100000 transactions inserted successfully!")

cursor.close()
conn.close()