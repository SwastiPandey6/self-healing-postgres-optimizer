def parse_explain(plan):

    root = plan[0]["Plan"]

    node_type = root["Node Type"]

    if "Plans" in root:
        child_node = root["Plans"][0]
        node_type = child_node["Node Type"]

    return {

        "node_type": node_type,

        "startup_cost": root["Startup Cost"],

        "total_cost": root["Total Cost"],

        "actual_time": root["Actual Total Time"]

    }