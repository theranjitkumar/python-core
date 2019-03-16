import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["user"]

data = []

for x in mycol.find():
    data.append(x)
    # print(x)

print(data)    
