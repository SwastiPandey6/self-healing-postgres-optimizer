import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="optimizer_db",
        user="postgres",
        password="postgres",  # replace with your password
        port="5432"
    )

    print("Connected successfully!")

except Exception as e:
    print("Connection failed!")
    print(e)