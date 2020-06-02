import pymongo


class MongoDB:
    _instance = None
    client = pymongo.MongoClient(host = '172.17.0.3', port = 27017, username = 'root', password = 'wpdlwl')
    db = client.backend

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

    def find_one(self, collection_name, query):
        return self.db[collection_name].find_one(query)
