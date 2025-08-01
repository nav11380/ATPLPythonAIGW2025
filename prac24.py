#1.create coonection with mongodb
#2.select the databse and the collection,you wnat to work
#3.create write function(insert,delete ,update)
#4.create read function(retrieve /fetch)
#mongodb : find()
from pymongo.mongo_client import MongoClient
class MongoDBHelper:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://Navdeep:Navdeep%40123@cluster0.erimsax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print('[MongoDB] Connection Created :')

    def select_db(self, db_name = 'gw2025', collection= 'users'):
        self.db = self.client[db_name]
        self.collection = self.db[collection]
        print('[MongoDBHelper] DB{} Collection {} Selected'.format(db_name,collection))

    def insert(self,document):
        result = self.collection.insert_one(document)
        print('[MongoDBHelper]Document inserted in collection{}'.format(self.collection.name))
        return result

    def delete(self,query):
        result = self.collection.delete_one(query)
        print('[MongoDBHelper]Document [delete] in collection{}'.format(self.collection.name))
        return result
    
    def update(self,query,document):
        result = self.collection.update_one(query,{'$set':document})
        print('[MongoDBHelper]Document [updated] in collection{}'.format(self.collection.name))
        return result
    
    def fetch(self,query =''):
        document = self.collection.find(query)
        return list(document)




        
