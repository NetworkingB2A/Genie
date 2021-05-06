import pynetbox
import os
import requests
from pprint import pprint

netbox_token = os.getenv("NETBOX_TOKEN")
netbox_url = os.getenv("NETBOX_URL")

netbox = pynetbox.api(netbox_url, token=netbox_token)
devices = netbox.dcim.devices.all()
for device in devices:
    print(device)



#
#url = "http://angell-netbox:8000/api/dcim/devices/?tag=labprod"
#
#payload={}
#headers = {
#  'Content-Type': 'application/json',
#  'Authorization': 'Token b55fabbaa93e38f8fc762a32744ff0198662fc3f'
#}

#response = requests.request("GET", url, headers=headers, data=payload)
#test = response.json()['results']
#for number, device in enumerate(test):
#    pprint(test[number])