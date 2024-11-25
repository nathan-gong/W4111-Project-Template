from interactive_app.application.services.old.MySQLDataService import MySQLDataService


class NameBasicsDataService(MySQLDataService):

    def __init__(self, database_name, table_name, key_columns):
        super().__init__()

        self.database_name = database_name
        self.table_name = table_name
        self.key_column = key_column


    def get_by_primary_key(self, primary_key_value):
        sql = f"select * from {self.database_name}.{self.table_name} "
        where_clause = f" where {self.key_column}=%s"
