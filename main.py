import firestore_main
import raspberry_main

number_of_testing_points=int(input('number of testing points'))
number_of_mes=10


for i in range(number_of_testing_points):
    ID=str(input("ID "))
    firestore_main.add_rssi(raspberry_main.get_apinfo(number_of_mes),ID)

