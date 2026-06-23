import psycopg2
import json

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()

query = """
SELECT *
FROM orders
WHERE customer_id = 1000;
"""

cursor.execute(
    "EXPLAIN (ANALYZE, FORMAT JSON) " + query
)

result = cursor.fetchone()[0]


def parse_explain(plan):

    plan = plan[0]["Plan"]

    return {
        "node_type": plan["Node Type"],
        "startup_cost": plan["Startup Cost"],
        "total_cost": plan["Total Cost"],
        "actual_time": plan["Actual Total Time"]
    }


parsed = parse_explain(result)

def detect_seq_scan(parsed_plan):

    if parsed_plan["node_type"] == "Seq Scan":
        return {
            "problem": "Sequential Scan detected",
            "severity": "HIGH"
        }

    return {
        "problem": "No issue",
        "severity": "LOW"}


warning = detect_seq_scan(parsed)

print("\nPARSED PLAN:")
print(parsed)

print("\nWARNING:")
print(warning)

cursor.close()
conn.close()