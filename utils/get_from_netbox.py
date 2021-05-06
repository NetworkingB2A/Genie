import pynetbox
import os
import requests
from pprint import pprint

netbox_token = os.getenv("NETBOX_TOKEN")
netbox_url = os.getenv("NETBOX_URL")

netbox = pynetbox.api(netbox_url, token=netbox_token)
devices = netbox.dcim.devices.filter(role=["lab-router", "lab-switch"])
#devices = netbox.dcim.devices.all()
for device in devices:
    pprint(dict(device))
    print(device.custom_fields["ansible_password"])
    testbed= {"name": device.display_name, "ip address": device.primary_ip["address"]}
    print (testbed)

