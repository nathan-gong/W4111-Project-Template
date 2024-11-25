import pymysql


class MySQLDataService:

    def __init__(self):
        self.user = "root"
        self.password = "dbuserdbuser"
        self.cursorclass = pymysql.cursors.DictCursor
        self.host = "localhost"
        self.autocommit = True
        self.port = 3306

    def get_connection(self):

        result = pymysql.connect(
            user=self.user,
            password=self.password,
            cursorclass=self.cursorclass,
            host=self.host,
            port = self.port,
            autocommit=self.autocommit
        )
        return result

    def run_q(self, q, args=None, conn=None, cursor=None, fetch=False, commit=True):
        """
        Method to run queries on your MySQL Database.

        :param q: The query string
        :param args: Any arguments passed
        :param conn: A database connection if there is one to use.
        :param cursor: A cursor to use if there is one.
        :param fetch: Whether the query needs to return data
        :return: Result from query. This is either the result of the query or the data.
        """

        result = None
        cursor_created = False
        connection_created = True

        if conn is None:
            conn = self.get_connection()
            cursor = conn.cursor()

            connection_created=True
            cursor_created = True

        full_sql = cursor.mogrify(q, args)
        print("MySQLDataService.run_q: Q = ", q)

        try:
            result = cursor.execute(q, args)
            if fetch:
                result = cursor.fetchall()

            if commit:
                conn.commit()

            if connection_created:
                conn.close()
            elif cursor_created:
                cursor.close()

        except Exception as e:
            if connection_created:
                conn.close()
            elif cursor_created:
                cursor.close()

            # A real system would let the calling code determine if the failure should trigger rollback.
            # We trigger rollback to avoid database locks.
            conn.rollback()

        return result

    def get_by_template(self, database_name, table_name, template, fields=None):

        sql = f"select * from {database_name}.{table_name} "

        if template:
            where_terms = []
            args = []
            where_clause = " where "

            for k, v in template.items():
                where_terms.append(f"{k} = %s")
                args.append(v)

            where_clause += " and ".join(where_terms)
            sql += where_clause
        else:
            args=None

        result = self.run_q(sql, args, fetch=True)

        return result



