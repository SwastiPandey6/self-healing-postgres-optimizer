def generate_html_report(
        problem,
        index_name,
        before_time,
        after_time,
        improvement):

    html = f"""
    <!DOCTYPE html>

    <html>

    <head>

    <title>Optimization Report</title>

    <style>

    body {{
        font-family: Arial;
        margin:40px;
        background-color:#f4f6f9;
    }}

    .card {{
        background:white;
        padding:20px;
        border-radius:10px;
        box-shadow:0px 0px 10px gray;
        width:600px;
    }}

    h1 {{
        color:#2E86C1;
    }}

    table {{
        width:100%;
        border-collapse:collapse;
    }}

    td {{
        padding:15px;
        border-bottom:1px solid lightgray;
    }}

    </style>

    </head>

    <body>

    <div class="card">

    <h1>Self-Healing PostgreSQL Optimization Report</h1>

    <table>

    <tr>
    <td><b>Problem</b></td>
    <td>{problem}</td>
    </tr>

    <tr>
    <td><b>Index Added</b></td>
    <td>{index_name}</td>
    </tr>

    <tr>
    <td><b>Before Time</b></td>
    <td>{before_time:.2f} ms</td>
    </tr>

    <tr>
    <td><b>After Time</b></td>
    <td>{after_time:.2f} ms</td>
    </tr>

    <tr>
    <td><b>Improvement</b></td>
    <td>{improvement:.2f}%</td>
    </tr>

    </table>

    </div>

    </body>

    </html>
    """

    with open(
            "optimization_report.html",
            "w",
            encoding="utf-8"
    ) as file:

        file.write(html)