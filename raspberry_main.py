import rssi
import re

def get_MAC_RSSI(text):
    pattern='[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}'
    mac_addr_list = re.findall(pattern, text['output'])

    pattern='(?<=Signal level=).*?(?= dBm)' #oui
    rssi_list=re.findall(pattern, text['output'])

    rssi_list=[int(elm) for elm in rssi_list]

    output = dict(zip(mac_addr_list, rssi_list))

    return output

interface = 'wlan0' #ip link show
rssi_scanner = rssi.RSSI_Scan(interface)

def get_apinfo(n=10):
    result_tmp={}
    for i in range(n):
        ap_info = rssi_scanner.getRawNetworkScan()
        ap_info=get_MAC_RSSI(ap_info['output'])

        if len(result_tmp.keys())==0:
            result_tmp=ap_info
        else:
            for mac in ap_info:
                result_tmp[mac]=result_tmp[mac]+ap_info[mac]

    for key in result_tmp:
         result_tmp[key]=result_tmp[key]/n

    return result_tmp

if __name__=='__main__':
    ap_info = rssi_scanner.getRawNetworkScan()
    print(ap_info)
