def insert_history(
    cursor,
    problem,
    recommendation,
    before_time,
    after_time,
    improvement
):

    cursor.execute(
        """
        INSERT INTO optimization_history(
        problem,
        recommendation,
        before_time,
        after_time,
        improvement,
        created_at
        )

        VALUES(
        %s,%s,%s,%s,%s,NOW()
        )
        """,

        (
            problem,
            recommendation,
            before_time,
            after_time,
            improvement
        )
    )