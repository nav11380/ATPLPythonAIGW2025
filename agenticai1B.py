from prac24 import MongoDBHelper


def get_questions():
    db = MongoDBHelper
    db.select_db(db_name= 'gw2025', collection= ' questions')
    return list(db.fetch())