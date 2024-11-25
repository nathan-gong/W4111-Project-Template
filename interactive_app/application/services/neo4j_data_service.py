#
# DFF TODO: Accessing database directly from resource is an anti-pattern.
# You did not learn this from me.
#
from resources.base_data_service import BaseDataService
from py2neo import Graph, NodeMatcher, RelationshipMatcher


class Neo4jDataService(BaseDataService):

    def __init__(self, config_info):
        super().__init__(config_info)
        self.confg_info.db_url = config_info.db_url

    def _get_connection(self):
        """
        :return:
        """
        if self.connection is None:
            db_url = self.confg_info.db_url
            auth = self.confg_info.auth

            self.connection = Graph(db_url, auth=auth)

        return self.connection

    def _close_connection(self):
        """

        :return:
        """
        pass

    def _get_collection(self, collection_name):
        pass

    def _get_db(self):
        pass

    def get_by_template(self,
                        collection_name,
                        template=None,
                        field_list=None
                        ):

        conn = self._get_connection()
        nm = NodeMatcher(conn)
        res = nm.match(collection_name, **template)

        result = []
        for r in res:
            result.append(r)
            
        return result

    def list_resources(self):
        q = "MATCH (n) RETURN distinct labels(n)"
        conn = self._get_connection()
        result = conn.run(q)
        result = result.data()

        return result

    def get_related_resources(self,
                              collection_name,
                              source_template=None,
                              relationship_label=None,
                              relationship_template=None):

        nodes = self.get_by_template(collection_name, source_template)
        r_matcher = RelationshipMatcher(self._get_connection())

        if relationship_template:
            result = r_matcher.match(nodes, relationship_template, **relationship_template)
        else:
            result = r_matcher.match(nodes, relationship_template)

        final_result = []
        for r in result:
            tmp = {"relationship":
                       { "type": list(r.types()),
                         "properties": dict(r),
                         },
                   "target_node": {
                       "type": r.end_node.labels,
                       "properties": dict(r.end_node)
                   }
                   }
            final_result.append(tmp)


        return final_result
