import psycopg2
import json

# -------------------------------
# Database Connection
# -------------------------------

conn = psycopg2.connect(
    host="localhost",
    database="optimizer_db",
    user="postgres",
    password="postgres",  # Change if your password is different
    port="5432"
)

cursor = conn.cursor()

# -------------------------------
# Query to Analyze
# -------------------------------

query = """
SELECT *
FROM orders
WHERE customer_id = 1000;
"""

# -------------------------------
# Execute EXPLAIN ANALYZE
# -------------------------------

cursor.execute(
    "EXPLAIN (ANALYZE, FORMAT JSON) " + query
)

result = cursor.fetchone()[0]

# -------------------------------
# Explain Parser
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
# Sequential Scan Detector
# -------------------------------

def detect_seq_scan(parsed_plan):

    if parsed_plan["node_type"] == "Seq Scan":
        return {
            "problem": "Sequential Scan detected",
            "severity": "HIGH"
        }

    return {
        "problem": "No issue detected",
        "severity": "LOW"
    }


# -------------------------------
# Cost Severity Detector
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
# Process Execution Plan
# -------------------------------

parsed = parse_explain(result)

warning = detect_seq_scan(parsed)

cost_severity = detect_cost_severity(parsed)

# -------------------------------
# Display Results
# -------------------------------

print("\n========== PARSED PLAN ==========")
print(parsed)

print("\n========== WARNING ==========")
print(warning)

print("\n========== COST SEVERITY ==========")
print(cost_severity)

# -------------------------------
# Cleanup
# -------------------------------

cursor.close()
conn.close()