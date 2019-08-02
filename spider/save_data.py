from pymongo import MongoClient
from config import MONGO_HOST,MONGP_PORT,MONGO_DB,MONGO_COLLECTION

class SaveData:
    def __init__(self):
        client = MongoClient(host=MONGO_HOST,port=MONGP_PORT)
        self.collection = client[MONGO_DB][MONGO_COLLECTION]

    def save_to_db(self,content_list):
        if isinstance(content_list,list):
            for content in content_list:
                self.collection.insert(content)
        elif isinstance(content_list,dict):
            self.collection.insert(content_list)
        print("save success")

_mongo_client = SaveData()
mongo_client = _mongo_client