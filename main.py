import firestore_main
import raspberry_main
import time

collection=int(input('number of collections '))
number_of_measurements=10

for sections in range(collection):
    collection_name=str(input('collection name'))
    number_of_rooms=int(input('number of rooms '))
    for i in range(number_of_rooms):
        number_of_testing_points=int(input('number of testing points '))
        for j in range(number_of_testing_points):
            ID=str(input("ID "))
            #time.sleep(5)
            firestore_main.add_rssi(raspberry_main.get_apinfo(number_of_measurements),ID,collection_name)

