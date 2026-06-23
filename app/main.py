import psycopg2
import re
import time

# -------------------------------
# Database Connection
# -------------------------------

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",
    port="5432"
)

conn.autocommit = True

cursor = conn.cursor()

query = """
SELECT *
FROM orders
WHERE customer_id = 1000;
"""

# -------------------------------
# Benchmark BEFORE
# -------------------------------

start = time.time()

cursor.execute(query)
cursor.fetchall()

end = time.time()

before_time = (end-start)*1000

# -------------------------------
# EXPLAIN ANALYZE
# -------------------------------

cursor.execute(
    "EXPLAIN (ANALYZE, FORMAT JSON) " + query
)

result = cursor.fetchone()[0]

# -------------------------------
# Parser
# -------------------------------

def parse_explain(plan):

    plan = plan[0]["Plan"]

    return {
        "node_type": plan["Node Type"],
        "total_cost": plan["Total Cost"],
        "actual_time": plan["Actual Total Time"]
    }


# -------------------------------
# Seq Scan Detector
# -------------------------------

def detect_seq_scan(parsed_plan):

    if parsed_plan["node_type"] == "Seq Scan":
        return True

    return False


# -------------------------------
# Recommendation Engine
# -------------------------------

def recommend_index(sql_query):

    table_match = re.search(
        r'FROM\s+(\w+)',
        sql_query,
        re.IGNORECASE
    )

    column_match = re.search(
        r'WHERE\s+(\w+)',
        sql_query,
        re.IGNORECASE
    )

    table_name = table_match.group(1)
    column_name = column_match.group(1)

    index_name = f"idx_{column_name}"

    return index_name, table_name, column_name


parsed = parse_explain(result)

if detect_seq_scan(parsed):

    index_name, table_name, column_name = recommend_index(query)

    create_index_sql = f"""
    CREATE INDEX CONCURRENTLY IF NOT EXISTS
    {index_name}
    ON {table_name}({column_name});
    """

    print("\nCreating Index...")

    cursor.execute(create_index_sql)

# -------------------------------
# Benchmark AFTER
# -------------------------------

start = time.time()

cursor.execute(query)
cursor.fetchall()

end = time.time()

after_time = (end-start)*1000

improvement = (
    (before_time-after_time)/before_time
)*100

# -------------------------------
# Results
# -------------------------------

print("\n========== RESULTS ==========")

print(f"Before : {before_time:.2f} ms")

print(f"After : {after_time:.2f} ms")

print(f"Improvement : {improvement:.2f}%")

cursor.close()
conn.close()