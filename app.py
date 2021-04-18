from flask import Flask, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
from io import StringIO

#CONSTS
DB_ACCESS_CODE_ = "./db_access_code_.json"
COLLECTION_NAME_ = "users_info"
DOCUMENT_NAME_ = "hKIT8opmXHmDC3jjUvxO"


# Preprocess request - check dtype from db
class RequestPreprocessing(object):
    db = None

    def __init__(self):
        cred = credentials.Certificate(DB_ACCESS_CODE_)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def db_test_add(self):
        user_data = {'user_key' : ['some_hash'], 'dtype' : ['json']}
        self.db.collection(COLLECTION_NAME_).document(DOCUMENT_NAME_).set(user_data)
        user_data = {'user_key' : firestore.ArrayUnion(["some_hash1"]), 'dtype' : firestore.ArrayUnion(["image"])}
        self.db.collection(COLLECTION_NAME_).document(DOCUMENT_NAME_).update(user_data)
        user_data = {'user_key' : firestore.ArrayUnion(["some_hash2"]), 'dtype' : firestore.ArrayUnion(["sound"])}
        self.db.collection(COLLECTION_NAME_).document(DOCUMENT_NAME_).update(user_data)
    
    def get_users_dtype(self, user_key):
        doc = self.db.collection(COLLECTION_NAME_).document(DOCUMENT_NAME_).get()
        if doc.exists:
            doc = doc.to_dict()
            if user_key in doc['user_key']:
                return doc['dtype'][doc['user_key'].index(user_key)]
        return None
    
    def user_data_saver(self, user_key, user_dtype, user_data):
        pass

    def user_data_processor(self, user_dtype, user_data):
        if user_dtype == 'json':
            io = StringIO(user_data)
            data = json.load(io)
            return data
    



#request getter
app = Flask(__name__)
requet_prsep = RequestPreprocessing()

@app.route('/')
def query():
    #request_prep.db_test_add()
    user_key = request.args.get('key')
    user_dtype = request_prep.get_users_dtype(user_key)

    user_data = request.args.get('data')
    user_data = request_prep.user_data_processor(user_dtype, user_data)

    return "project_huinya"

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    