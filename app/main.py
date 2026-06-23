import psycopg2

from parser.explain_parser import parse_explain
from detector.seq_scan_detector import detect_seq_scan
from detector.cost_detector import detect_cost_severity
from advisor.index_recommender import recommend_index
from optimizer.index_executor import execute_index
from benchmark.before_after_benchmark import benchmark_query
from report.json_report_generator import generate_json_report
from report.html_report_generator import generate_html_report
from history.history_manager import insert_history


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
WHERE customer_id=1000;
"""

before_time = benchmark_query(cursor, query)

cursor.execute(
    "EXPLAIN (ANALYZE, FORMAT JSON) " + query
)

result = cursor.fetchone()[0]

parsed = parse_explain(result)

cost_severity = detect_cost_severity(parsed)

problem = "No Problem"

index_name = "No New Index Created"

if detect_seq_scan(parsed):

    problem = "Sequential Scan"

    index_name, table_name, column_name = recommend_index(query)

    execute_index(
        cursor,
        index_name,
        table_name,
        column_name
    )

after_time = benchmark_query(cursor, query)

improvement = (
    (before_time - after_time)
    / before_time
) * 100

generate_json_report(
    problem,
    index_name,
    before_time,
    after_time,
    improvement
)

generate_html_report(
    problem,
    index_name,
    before_time,
    after_time,
    improvement
)

insert_history(
    cursor,
    query,
    problem,
    index_name,
    before_time,
    after_time,
    improvement
)

conn.commit()

print("\n========== RESULTS ==========")

print("Problem :", problem)

print("Cost Severity :", cost_severity)

print("Index :", index_name)

print(f"Before : {before_time:.2f} ms")

print(f"After : {after_time:.2f} ms")

print(f"Improvement : {improvement:.2f}%")

print("\nReports Generated!")

cursor.close()
conn.close()