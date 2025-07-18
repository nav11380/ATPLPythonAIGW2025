from pymongo.mongo_client import MongoClient
from Session23A import User

def main():
    uri = "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri)
    print('1. Connection Created with MongoDB :)')

    # query = {'email': 'jas@example.com'}
    # db = client['gw2025']
    # result = db['users'].delete_one(query)
    # print('result:', result)

    document = {'name': 'Johnny Smith', 'email': 'johnny.smith@example.com', 'address': 'Beverly Hills'}
    query = {'email': 'jonny@example.com'}
    db = client['gw2025']
    result = db['users'].update_one(query, {'$set':document})
    print('result:', result)

    
if __name__ == '__main__':
    main()