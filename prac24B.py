from prac24 import MongoDBHelper
from prac24A import User

def main():
    
    db_helper = MongoDBHelper()
    #db_helper.select_db()
    db_helper.select_db(db_name='gw2025', collection= 'users')

    user = User()
    user.input_user_details()
    user.show()

    result = db_helper.insert(document=user.to_document())
    print('user saved in MongoDB with _id as:',result.inserted_id)

if __name__ == '__main__':
    main()
