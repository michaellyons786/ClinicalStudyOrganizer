
class Query_Result:
    def __init__(self, query_result, attribute_names, is_identity=False):
        self.key_attributes = {}

        if not is_identity:
            self.attributes_names = attribute_names
            self._initialize(query_result)

    def _initialize(self, query_result):
        for row in query_result:
            alias = row[0]
            attributes = row[1:]

            self.key_attributes[alias] = attributes

    def get_aliases(self):
        return list(self.key_attributes.keys())

    def get_attributes(self, alias):
        return self.key_attributes[alias]

