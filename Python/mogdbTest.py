import pymongo

# Create a MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the 'test' database
db = client['test']

# Access the 'testcoll' collection
collection = db['testcoll']
"""
# Insert multiple documents into the collection
data_list = [
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40}
]
insert_results = collection.insert_many(data_list)
print(f"Inserted {len(insert_results.inserted_ids)} documents")
"""
# Find all documents in the collection
all_documents = collection.find()
print("All documents in the collection:")
for doc in all_documents:
    print(doc)

# Update multiple documents in the collection
update_query = {"age": {"$lt": 30}}
new_values = {"$set": {"status": "Young"}}
update_results = collection.update_many(update_query, new_values)
print(f"Modified {update_results.modified_count} documents")


# Delete all documents with age greater than 35
delete_query = {"age": {"$gt": 35}}
delete_results = collection.delete_many(delete_query)
print(f"Deleted {delete_results.deleted_count} documents")

# Close the MongoDB client  
client.close()  