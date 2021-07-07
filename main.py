import firestore_main
import raspberry_main

n=10
x='A'
y='1'
location='ROOM-1'+x+' '+y

firestore_main.add_rssi(raspberry_main.get_apinfo(n),location)