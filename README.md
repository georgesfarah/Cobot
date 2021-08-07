### Introduction

Cobot is a smart robot to serve Covid 19 patients without putting healthcare workers in risk of infection.

This repository is a collection of script used to localize the robot indoors using the RSSI of the Access Points.

### Content

##### This repo is a collection of scripts:

- *firestore_main.py* is used to interact with firestore: save data,get data and converting firestore collections to csv files.
- The csv files are stored in Datasets.

- *raspberry_main.py* is used to measure RSSI of the Access Points.
- *main.py* is run on raspberry pi and use the 2 scripts mentioned above to collect the data and store it.
- *Models/* contains scripts of different machine learning algorithms.

### Note:
You need *secret.json* to access the firestore database.