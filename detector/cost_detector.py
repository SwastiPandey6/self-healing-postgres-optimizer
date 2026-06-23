def detect_cost_severity(parsed_plan):

    cost = parsed_plan["total_cost"]

    if cost > 10000:
        return "HIGH"

    elif cost > 1000:
        return "MEDIUM"

    else:
        return "LOW"