# Self-Healing PostgreSQL Optimization Engine

## Overview

A self-healing database optimization engine that automatically detects sequential scans, recommends indexes, applies CREATE INDEX CONCURRENTLY, benchmarks performance, and generates reports.

---

## Features

- EXPLAIN ANALYZE Parser
- Sequential Scan Detection
- Cost Severity Detection
- Index Recommendation Engine
- Automatic Concurrent Index Creation
- Benchmark Engine
- JSON Report Generation
- HTML Report Generation
- Streamlit Dashboard
- Optimization History Tracking

---

## Tech Stack

- Python
- PostgreSQL
- psycopg2
- Streamlit
- Pandas
- Matplotlib

---

## Architecture

Query
↓
EXPLAIN ANALYZE
↓
Parser
↓
Seq Scan Detector
↓
Cost Detector
↓
Index Recommendation
↓
CREATE INDEX CONCURRENTLY
↓
Benchmark Engine
↓
Report Generator
↓
Dashboard

---

## Results

Before : 85.12 ms

After : 3.61 ms

Improvement : 95.76%

---

## Folder Structure

app/
database/
parser/
detector/
advisor/
optimizer/
benchmark/
history/
report/
dashboard/

---

## Future Scope

Version 2:
Autonomous PostgreSQL Performance Advisor using pg_stat_statements and Machine Learning.