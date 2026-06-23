import json


def generate_json_report(
        problem,
        index_name,
        before_time,
        after_time,
        improvement):

    report = {

        "problem": problem,

        "index_added": index_name,

        "before_time": round(before_time, 2),

        "after_time": round(after_time, 2),

        "improvement_percent": round(improvement, 2)

    }

    with open(
            "optimization_report.json",
            "w") as file:

        json.dump(
            report,
            file,
            indent=4)

    return report