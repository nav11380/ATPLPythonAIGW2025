import pymongo
from pymongo.mongo_client import MongoClient
from prac23A import User

def main():
    uri = "mongodb+srv://Navdeep:Navdeep%40123@cluster0.erimsax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    print('1.Connection Created With MongoDB:')

    user = User()
    user.input_user_details()
    user.show()
    print('2. User Created with Data :)')

    user_document = user.to_document()
    print(user_document)
    print('3. User Converted to Document/Dictionary :)')

    # Use Database:
    db = client['gw2025']

    # Insert Operation
    result = db['users'].insert_one(user_document)
    print('4. User Document Saved in MongoDB :)')
    print('result:', result, type(result))

    # Fetch Operation
    documents = db['users'].find()
    for documet in documents:
        print(documet)

if __name__ ==  '__main__':
    main()



    