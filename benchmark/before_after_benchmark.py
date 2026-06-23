import time


def benchmark_query(cursor, query):

    start = time.time()

    cursor.execute(query)

    cursor.fetchall()

    end = time.time()

    return (end - start) * 1000