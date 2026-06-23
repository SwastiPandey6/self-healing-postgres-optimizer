def detect_seq_scan(parsed_plan):

    return "Seq Scan" in parsed_plan["node_type"]