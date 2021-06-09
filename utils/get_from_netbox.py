import pynetbox
import os
import requests
from pprint import pprint

# thought
# Would it be better to make this a class so i can really return an custom object vs a dictionary type??


# I created a environmental Variable for a token and my URL
netbox_token = os.getenv("NETBOX_TOKEN")
netbox_url = os.getenv("NETBOX_URL")


# API call to my netbox
netbox = pynetbox.api(netbox_url, token=netbox_token)

# Here i called out my roles for my devices for my netbox
# TODO: need to make this more dynamic so I don't have the static entries
# devices = netbox.dcim.devices.filter(role=["lab-router", "lab-switch"])
devices = netbox.dcim.devices.filter(role="lab-router")

# This dictionary is needed to make pyATS happy
testbed = {"devices": {}}

# This part is creating the testbest for each device
# I can make this more dynamic if need be
# I have some custom fields in Netbox like the Ansible uname and password
def netboxget():
    for device in devices:
        testbedDevice = {
            device.display_name: {
                "connections": {
                    "cli": {
                        "ip": device.primary_ip["address"].split("/24")[0],
                        "protocol": "ssh",
                    }
                },
                "credentials": {
                    "default": {
                        "password": device.custom_fields["ansible_password"],
                        "username": device.custom_fields["ansible_uname"],
                    },
                    "enable": {"password": device.custom_fields["ansible_uname"]},
                },
                "os": device.platform["slug"],
                "type": device.platform["slug"],
            }
        }

        testbed["devices"].update(testbedDevice)
    return testbed
