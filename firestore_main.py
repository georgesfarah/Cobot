import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# https://faun.pub/getting-started-with-firebase-cloud-firestore-using-python-c6ab3f5ecae0
# https://firebase.google.com/docs/admin/setup?authuser=0#python


# Use the application default credentials
cred = credentials.Certificate('secret.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def add_rssi(dict_rssi,location):
    dict_rssi['location']=location
    db.collection('RSSIs').add(dict_rssi)


def get_RSSIs():
    snapshots = list(db.collection(u'RSSIs').get())
    for snapshot in snapshots:
        print(snapshot.to_dict())

if __name__=='__main__':
    print(get_RSSIs())