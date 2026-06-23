def generate_html_report(
        problem,
        index_name,
        before_time,
        after_time,
        improvement):

    html = f"""

    <html>

    <body>

    <h1>Optimization Report</h1>

    <hr>

    <h2>Problem</h2>

    <p>{problem}</p>

    <h2>Index Added</h2>

    <p>{index_name}</p>

    <h2>Before</h2>

    <p>{before_time:.2f} ms</p>

    <h2>After</h2>

    <p>{after_time:.2f} ms</p>

    <h2>Improvement</h2>

    <p>{improvement:.2f}%</p>

    </body>

    </html>

    """

    with open(

            "optimization_report.html",

            "w",

            encoding="utf-8"

    ) as file:

        file.write(html)