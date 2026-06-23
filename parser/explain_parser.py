def parse_explain(plan):

    plan = plan[0]["Plan"]

    return {
        "node_type": plan["Node Type"],
        "startup_cost": plan["Startup Cost"],
        "total_cost": plan["Total Cost"],
        "actual_time": plan["Actual Total Time"]
    }