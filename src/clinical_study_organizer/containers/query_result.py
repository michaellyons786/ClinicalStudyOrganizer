
class Query_Result:
    def __init__(self, query_result, attributes, isIdentity=False):
        self.key_attributes = {}

        if not isIdentity:
            self.attributes_names = attributes
            self._initialize(query_result)

    def _initialize(self, query_result):
        for row in query_result:
            alias = row[0]
            attributes = row[1:]

            self.key_attributes[alias] = attributes

