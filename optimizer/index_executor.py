def execute_index(
        cursor,
        index_name,
        table_name,
        column_name):

    sql = f"""
    CREATE INDEX CONCURRENTLY IF NOT EXISTS
    {index_name}
    ON {table_name}({column_name});
    """

    cursor.execute(sql)