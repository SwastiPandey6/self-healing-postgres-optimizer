import psycopg2
import re

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
# Explain Analyze
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
        "startup_cost": plan["Startup Cost"],
        "total_cost": plan["Total Cost"],
        "actual_time": plan["Actual Total Time"]
    }


# -------------------------------
# Seq Scan Detector
# -------------------------------

def detect_seq_scan(parsed_plan):

    if parsed_plan["node_type"] == "Seq Scan":
        return {
            "problem": "Sequential Scan detected",
            "severity": "HIGH"
        }

    return {
        "problem": "No issue",
        "severity": "LOW"
    }


# -------------------------------
# Cost Detector
# -------------------------------

def detect_cost_severity(parsed_plan):

    cost = parsed_plan["total_cost"]

    if cost > 10000:
        return "HIGH"

    elif cost > 1000:
        return "MEDIUM"

    return "LOW"


# -------------------------------
# Index Recommendation Engine
# -------------------------------

def recommend_index(sql_query):

    table_match = re.search(r'FROM\s+(\w+)', sql_query, re.IGNORECASE)

    column_match = re.search(
        r'WHERE\s+(\w+)',
        sql_query,
        re.IGNORECASE
    )

    if table_match and column_match:

        table_name = table_match.group(1)

        column_name = column_match.group(1)

        index_name = f"idx_{column_name}"

        recommendation = (
            f"CREATE INDEX {index_name} "
            f"ON {table_name}({column_name});"
        )

        return recommendation

    return "No recommendation"


# -------------------------------
# Processing
# -------------------------------

parsed = parse_explain(result)

warning = detect_seq_scan(parsed)

cost_severity = detect_cost_severity(parsed)

index_recommendation = recommend_index(query)

# -------------------------------
# Output
# -------------------------------

print("\n========== PARSED PLAN ==========")
print(parsed)

print("\n========== WARNING ==========")
print(warning)

print("\n========== COST SEVERITY ==========")
print(cost_severity)

print("\n========== INDEX RECOMMENDATION ==========")
print(index_recommendation)

cursor.close()
conn.close()