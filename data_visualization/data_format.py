from pymongo import MongoClient
from config import MONGO_HOST,MONGP_PORT,MONGO_DB,MONGO_COLLECTION

def choose_data():
    """处理数据，提取有用字段"""
    client = MongoClient(host=MONGO_HOST,port=MONGP_PORT)
    collection = client[MONGO_DB][MONGO_COLLECTION]
    db_data = collection.find()
    data_list = []
    for data in db_data:
        item = {}
        # 国家
        item["country"] = data["tv_category"]
        #电视剧的名字
        item["title"] = data["title"]
        #导演
        item["directors"] = "_".join(data["directors"])
        #演员
        item["actors"] = "_".join(data["actors"])

        directors_actors_list = data["directors"]
        directors_actors_list.extend(data["actors"])

        # 提取时间
        if data["release_date"]:
            release_data = data["release_date"].split(".")
            item["release_date"] = data["year"] + "-" + release_data[0] + "-" + release_data[1]
        else:
            item["release_date"] = None

        # 提取分类
        tag_list = data["info"].split(" / ")[1].split(" ")
        item["tag"] = "_".join(tag_list)
        #打分的人数
        if data["rating"] :
            item["rating_count"] = data["rating"]["count"]
        #分数
            item["rating_value"] = data["rating"]["value"]
        else:
            item["rating_count"] = None
        # 分数
            item["rating_value"] = None
        data_list.append(item)

    return data_list

if __name__ == "__main__":
    data_list = choose_data()
    for i in data_list:
        print(i["tag"], "***", i["release_date"])
    print(data_list)