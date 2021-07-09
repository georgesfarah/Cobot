from typing import Collection
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv
import pandas as pd
# https://faun.pub/getting-started-with-firebase-cloud-firestore-using-python-c6ab3f5ecae0
# https://firebase.google.com/docs/admin/setup?authuser=0#python


# Use the application default credentials
cred = credentials.Certificate('secret.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def add_rssi(dict_rssi,location):
    dict_rssi['location']=location
    db.collection('RSSIs').add(dict_rssi)

def get_header(snapshots):
    results=[]
    for snapshot in snapshots:
        keys=snapshot.to_dict().keys()
        for key in keys:
            if key not in results:
                results.append(key)
    return results

def gen_snapshots_list(header,snapshots):
    out=[]
    for snapshot in snapshots:
        dic=snapshot.to_dict()
        for h in header:
            if h not in dic:
                dic[h]=''
        out.append(dic)

    return out

def genCSV(header,snapshots_list,collection_name):
    csv_file=collection_name+'.csv'
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for data in snapshots_list:
            writer.writerow(data)
        


def get_RSSIs(collection_name):
    snapshots = list(db.collection(collection_name).get())
    header=get_header(snapshots)
    snapshots_list=gen_snapshots_list(header,snapshots)
    genCSV(header,snapshots_list,collection_name)

if __name__=='__main__':
    collections=db.collections()
    l=[]
    for col in collections:
        l.append(col.id)
    
    for collection in l:
        get_RSSIs(collection)