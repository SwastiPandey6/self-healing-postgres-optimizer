def insert_history(
        cursor,
        query_text,
        problem,
        recommendation,
        before_time,
        after_time,
        improvement):

    cursor.execute(

        """
        INSERT INTO optimization_history(

        query,

        problem,

        recommendation,

        before_time,

        after_time,

        improvement,

        created_at

        )

        VALUES(

        %s,%s,%s,%s,%s,%s,NOW()

        )
        """,

        (

            query_text,

            problem,

            recommendation,

            before_time,

            after_time,

            improvement

        )

    )