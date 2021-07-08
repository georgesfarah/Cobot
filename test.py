import firestore_main
import raspberry_main

print('a')



output={
        'output':'''wlp1s0    Scan completed :
      Cell 01 - Address: A0:3D:6F:26:77:8E
                Channel:144
                Frequency:5.72 GHz
                Quality=43/70  Signal level=-67 dBm  
                Encryption key:on
                ESSID:"ucrwpa"
                Bit Rates:24 Mb/s; 36 Mb/s; 48 Mb/s; 54 Mb/s
                Mode:Master
      Cell 02 - Address: A0:3D:6F:26:77:82
                Channel:1
                Frequency:2.412 GHz (Channel 1)
                Quality=43/70  Signal level=-67 dBm  
                Encryption key:on
                ESSID:"eduroam"
                Bit Rates:18 Mb/s; 24 Mb/s; 36 Mb/s; 48 Mb/s; 54 Mb/s
                Mode:Master''',
        'error':''
    }

print(raspberry_main.get_MAC_RSSI(output))