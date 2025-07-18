"""
    
    Part 1:
    
    MongoDB -->> We are using MongoDB in cloud (MongoDB Atlas)
    -------
    1. Signup/Register
    2. Create a Cluster (AWS | GCP | Azure)
        GCP -> select region as Delhi
    3. Network Access ->> 0.0.0.0/0 (Access MongoDB from any IP Address)    
    4. Database Access ->> Create a User with Admin Role

    In MongoDB
    We dont have tables, we have Collections
    A collection is like a folder

    We dont have rows, we have Documents
    A document is typically a JSON Document, which gets stored inside the collection

    Hence, MongoDB is a NoSQL DataBase :)

    Part 2:
    How to connect to MongoDB from Python

    1. Install MongoDB Library
        python -m pip install "pymongo[srv]"

    2. Create Connection to MongoDB
        2.1 Create URI with username and password
        2.2 Create a MongoClient Object 
        2.3 Send a Ping Command to Test


"""


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client['gw2025']
collections = db.list_collection_names()
# print(collections)

print('{} collections found in database'.format(len(collections)))
for collection in collections:
    print(collection)

# documents = db['users'].find()
documents = list(db['users'].find())
print('{} documents found in users collection'.format(len(documents)))
for document in documents:
    print(document)
