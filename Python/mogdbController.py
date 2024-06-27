import pymongo
from bson import ObjectId, json_util
import json


def make_clientconnection():

    addr = '127.0.0.1'
    port = '27017'


    addr_complete = 'mongodb://' + addr + ':' + port + '/'  # 'mongodb://172.16.10.16:27017/'


    myclient = pymongo.MongoClient(addr_complete)

    return myclient


def make_dbconnection(myclient, db_name):
    dblist = myclient.list_database_names()

    mydb = myclient[db_name]


    return mydb


def make_collectionconnection(mydb, collection_name):

    col_list = mydb.list_collection_names()

    mycollection = mydb[collection_name]

    count = mycollection.count_documents({})


    return mycollection



def get_all_documents(db_name = 'lezione', collection_name = 'prova'):

    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    document = collection.find({})

    return json_util.dumps(document)


def get_user_document(user_id, db_name = 'lezione', collection_name = 'prova'):

    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    document = collection.find({"user_id":user_id})


    return json_util.dumps(document)


def create_document(nomedb = 'lezione', nomecollezione = 'prova', mydict = None):
    if mydict is None:
        mydict = {}

    client = make_clientconnection()
    db = make_dbconnection(client, nomedb)
    collection = make_collectionconnection(db, nomecollezione)



    x = collection.insert_one(mydict)
    new_id = str(x.inserted_id)
    return json.dumps({"id": new_id})




if __name__ == '__main__':

    test_doc = {
        "user_id":1993,
        "nome":"Gabriele",
        "cognome":"Gerbino"}

    create_document(mydict=test_doc)

    print(get_user_document(1993))
    print(get_all_documents())