import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('accountInfo.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

list_collection= db.collection('list').get()

#Print all items on the todo list currently
for doc in list_collection:
    print(doc.to_dict())
    # print(doc.to_dict()['description'])

