import firestore_main
import raspberry_main


collection=int(input('number of collections '))
number_of_mes=10

for sections in range(collection):
    collection_name=str(input('collection name'))
    number_of_testing_points=int(input('number of testing points '))
    for i in range(number_of_testing_points):
        ID=str(input("ID "))
        firestore_main.add_rssi(raspberry_main.get_apinfo(number_of_mes),ID,collection_name)

