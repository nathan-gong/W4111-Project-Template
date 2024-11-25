from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig


class ArtistMySQLDataService(MySQLDataService):

    def __init__(self, config: MySQLDataServiceConfig):
        super().__init__(config)

    def get_artist_all(self, nconst: str):
        sql = """
        
        
        
        """