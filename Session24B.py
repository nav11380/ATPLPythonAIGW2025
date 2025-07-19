from Session24 import MongoDBHelper
from Session24A import User

def main():
    
    db_helper = MongoDBHelper()
    # db_helper.select_db()
    db_helper.select_db(db_name='gw2025', collection='users')

    user = User()
    user.input_user_details()
    user.show()

    result = db_helper.insert(document=user.to_document())
    print('User Saved in MongoDB with _id as: ', result.inserted_id)

    # Implement -> delete, update and fetch with MongoDB Helper


if __name__ == '__main__':
    main()