# 🚀 Self-Healing PostgreSQL Optimization Engine

## Overview

Self-Healing PostgreSQL Optimization Engine is an automated database performance optimization system that analyzes query execution plans, detects performance bottlenecks, recommends indexes, applies concurrent indexing, benchmarks query execution, and generates reports with visualization dashboards.

The system mimics the functionality of database performance tools such as **pgHero**, **AWS Performance Insights**, and **pganalyze**, while focusing on automated optimization and self-healing capabilities.

---

## Features

* EXPLAIN ANALYZE execution plan parsing
* Sequential scan detection
* Cost severity analysis
* Automatic index recommendation
* CREATE INDEX CONCURRENTLY support
* Query benchmarking
* JSON report generation
* HTML report generation
* Optimization history tracking
* Streamlit dashboard visualization
* Modular architecture

---

## System Architecture

```text
Query
 ↓
EXPLAIN ANALYZE
 ↓
JSON Execution Plan
 ↓
Explain Parser
 ↓
Sequential Scan Detector
 ↓
Cost Severity Detector
 ↓
Index Recommendation Engine
 ↓
CREATE INDEX CONCURRENTLY
 ↓
Benchmark Engine
 ↓
Report Generation
 ↓
Optimization History
 ↓
Streamlit Dashboard
```

---

## Folder Structure

```text
postgres_optimizer/

├── app/
│   └── main.py

├── database/
│   ├── db_connector.py
│   └── data_generator.py

├── parser/
│   └── explain_parser.py

├── detector/
│   ├── seq_scan_detector.py
│   └── cost_detector.py

├── advisor/
│   └── index_recommender.py

├── optimizer/
│   └── index_executor.py

├── benchmark/
│   └── before_after_benchmark.py

├── report/
│   ├── json_report_generator.py
│   └── html_report_generator.py

├── history/
│   └── history_manager.py

├── dashboard/
│   ├── streamlit_dashboard.py
│   └── history_dashboard.py

└── data/
```

---

## Tech Stack

| Component       | Technology   |
| --------------- | ------------ |
| Language        | Python       |
| Database        | PostgreSQL   |
| Database Driver | psycopg2     |
| Visualization   | Streamlit    |
| Data Processing | Pandas       |
| Graphs          | Matplotlib   |
| Version Control | Git & GitHub |

---

## Workflow

1. Execute SQL query.
2. Obtain execution plan using EXPLAIN ANALYZE.
3. Parse execution plan.
4. Detect sequential scans.
5. Analyze query cost.
6. Recommend indexes.
7. Create indexes using CREATE INDEX CONCURRENTLY.
8. Benchmark query performance.
9. Generate reports.
10. Store optimization history.
11. Visualize results through Streamlit.

---

## Results

| Metric                  | Value           |
| ----------------------- | --------------- |
| Problem Detected        | Sequential Scan |
| Cost Severity           | High            |
| Index Added             | idx_customer_id |
| Before Optimization     | 85.12 ms        |
| After Optimization      | 3.61 ms         |
| Performance Improvement | 95.76 %         |

---

## Sample Output

```text
Problem : Sequential Scan

Cost Severity : HIGH

Index : idx_customer_id

Before : 85.12 ms

After : 3.61 ms

Improvement : 95.76%
```

---

## Dashboard

The project includes:

* Performance Dashboard
* Before vs After Analysis
* Optimization History Dashboard
* HTML Reports
* JSON Reports

---

## Future Scope

Version 2 will extend the system into an Autonomous PostgreSQL Performance Advisor by integrating:

* pg_stat_statements
* Multi-column index recommendation
* Machine Learning based optimization
* Query ranking
* Trend analysis
* Docker deployment
* REST APIs
* Cloud database support

---

## References

* PostgreSQL Documentation
* Streamlit Documentation
* psycopg2 Documentation
* pgHero
* AWS Performance Insights
* pganalyze

---

## Author

**Etash**
B.Tech CSE (Cyber Security)

---

Self-Healing PostgreSQL Optimization Engine | Version 1
