
class Query_Result:
    def __init__(self, query_result):
        self.key_values = {}
        self._initialize(query_result)

    def _initialize(self, query_result):
        for row in query_result:
            key = row[0]
            value = row[1:]

            self.key_values[key] = value

    def get(self, key):
        return self.key_values[key]

