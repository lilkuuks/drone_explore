# from multiprocessing.connection import Connection
import pymongo

def MongoConnection():
    global collection

    connection_string = "mongodb://localhost:27017/"

    # instance of MongoClient
    client = pymongo.MongoClient(connection_string)

    # Accessing the database
    db = client['dronedb2']

    # Accessing the collection
    collection = db['dronedbtest']
    sStatus:str = "Connection Established to MongoDB"

    return sStatus

MongoConnection()
if __name__ == '__main__':
    MongoConnection()

"""Test purpose"""
# def CheckBrand(brandname:str, ):
#     MongoConnection()
#     modelfind = {"brand": brandname}
#     for i in collection.find(modelfind):
#         print(i)
