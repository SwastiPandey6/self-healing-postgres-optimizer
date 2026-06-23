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