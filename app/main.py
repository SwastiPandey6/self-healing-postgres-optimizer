import psycopg2
import re
import time
import json

# -------------------------------
# Database Connection
# -------------------------------

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",  # change if different
    port="5432"
)

conn.autocommit = True

cursor = conn.cursor()

# -------------------------------
# Query
# -------------------------------

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

before_time = (end - start) * 1000

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

    root = plan[0]["Plan"]

    node_type = root["Node Type"]

    # Look inside child nodes
    if "Plans" in root:

        child_node = root["Plans"][0]

        node_type = child_node["Node Type"]

    return {

        "node_type": node_type,

        "startup_cost": root["Startup Cost"],

        "total_cost": root["Total Cost"],

        "actual_time": root["Actual Total Time"]

    }

# -------------------------------
# Seq Scan Detector
# -------------------------------

def detect_seq_scan(parsed_plan):

    return parsed_plan["node_type"] == "Seq Scan"

# -------------------------------
# Cost Detector
# -------------------------------

def detect_cost_severity(parsed_plan):

    cost = parsed_plan["total_cost"]

    if cost > 10000:
        return "HIGH"

    elif cost > 1000:
        return "MEDIUM"

    else:
        return "LOW"

# -------------------------------
# Index Recommendation Engine
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

# -------------------------------
# Process Plan
# -------------------------------

parsed = parse_explain(result)

cost_severity = detect_cost_severity(parsed)

index_name = "No New Index Created"

problem = "No Problem"

# -------------------------------
# Self Healing
# -------------------------------

if detect_seq_scan(parsed):

    problem = "Sequential Scan"

    index_name, table_name, column_name = recommend_index(query)

    create_index_sql = f"""
    CREATE INDEX CONCURRENTLY IF NOT EXISTS
    {index_name}
    ON {table_name}({column_name});
    """

    print("\nCreating Index...\n")

    cursor.execute(create_index_sql)

# -------------------------------
# Benchmark AFTER
# -------------------------------

start = time.time()

cursor.execute(query)
cursor.fetchall()

end = time.time()

after_time = (end - start) * 1000

improvement = (
    (before_time - after_time)
    / before_time
) * 100

# -------------------------------
# Results
# -------------------------------

print("\n========== PARSED PLAN ==========")
print(parsed)

print("\n========== COST SEVERITY ==========")
print(cost_severity)

print("\n========== RESULTS ==========")

print(f"Before : {before_time:.2f} ms")

print(f"After : {after_time:.2f} ms")

print(f"Improvement : {improvement:.2f}%")

# -------------------------------
# JSON Report Generation
# -------------------------------

report = {

    "problem": problem,

    "index_added": index_name,

    "before_time": round(before_time, 2),

    "after_time": round(after_time, 2),

    "improvement_percent": round(improvement, 2)

}

with open("optimization_report.json", "w") as file:

    json.dump(report, file, indent=4)

print("\nJSON Report Generated!")

# -------------------------------
# Cleanup
# -------------------------------

cursor.close()
conn.close()