import re


def recommend_index(sql_query):

    table_match = re.search(
        r'FROM\s+(\w+)',
        sql_query,
        re.IGNORECASE
    )

    column_match = re.search(
        r'WHERE\s+(\w+)',
        sql_query,
        re.IGNORECASE
    )

    table_name = table_match.group(1)

    column_name = column_match.group(1)

    index_name = f"idx_{column_name}"

    return index_name, table_name, column_name