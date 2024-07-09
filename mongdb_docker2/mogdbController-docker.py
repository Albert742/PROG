import pymongo
from bson.json_util import dumps
from pprint import pprint
import json


def make_clientconnection():
    addr = '127.0.0.1'
    port = '27027'

    addr_complete = f'mongodb://{addr}:{port}/'

    myclient = pymongo.MongoClient(addr_complete)

    return myclient


def make_dbconnection(myclient, db_name):
    mydb = myclient[db_name]

    return mydb


def make_collectionconnection(mydb, collection_name):
    mycollection = mydb[collection_name]

    return mycollection


def get_all_documents(db_name = 'prova', collection_name = 'prova'):
    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    document = collection.find({})

    return dumps(document)


def get_user_document(user_id, db_name = 'prova', collection_name = 'prova'):
    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    document = collection.find_one({"user_id":user_id})

    return dumps(document)


def create_document(nomedb = 'prova', nomecollezione = 'prova', mydict = None):
    if mydict is None:
        mydict = {}

    client = make_clientconnection()
    db = make_dbconnection(client, nomedb)
    collection = make_collectionconnection(db, nomecollezione)

    x = collection.insert_one(mydict)
    new_id = str(x.inserted_id)
    return {"id": new_id}


def update_document(document_id, db_name = 'prova', collection_name = 'prova', mydict = {}):
    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    x = collection.update_one({"_id": document_id}, {"$set": mydict})

    if x.modified_count == 1:
        return True
    else:
        return False


def delete_document(document_id, db_name = 'prova', collection_name = 'prova'):
    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    x = collection.delete_one({"_id": document_id})

    if x.deleted_count == 1:
        return True
    else:
        return False


def find_document(query_dict, db_name = 'prova', collection_name = 'prova'):
    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    document = collection.find(query_dict)

    return dumps(document)


def find_one_document(query_dict, db_name = 'prova', collection_name = 'prova'):
    client = make_clientconnection()
    db = make_dbconnection(client, db_name)
    collection = make_collectionconnection(db, collection_name)

    document = collection.find_one(query_dict)

    return dumps(document)


if __name__ == '__main__':
    documents = [
        {"user_id":1993, "nome":"Gabriele", "cognome":"Gerbino"},
        {"user_id":1992, "nome":"Alberto", "cognome":"Pizzamilgio"},
        {"user_id":1991, "nome":"Mario", "cognome":"Rossi"},
        {"user_id":1990, "nome":"Luigi", "cognome":"Verdi"},
        {"user_id":1989, "nome":"Marco", "cognome":"Bianchi"}
    ]

    client = make_clientconnection()
    db = make_dbconnection(client, 'lezione')
    collection = make_collectionconnection(db, 'prova')

    for doc in documents:
        create_document(mydict=doc)

    #print(get_user_document(1993))
    #print(get_all_documents())
