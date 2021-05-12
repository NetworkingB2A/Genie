#! ../venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup
from utils.get_from_netbox import netboxget
import csv

tb = load(netboxget())
#TODO: I think there is a better way to do this, may want to rewrite
count = 0
for device in  tb.devices:
    tempConnect = tb.devices[device]
    tempConnect.connect()
    ipRoutes = tempConnect.parse('show ip route ')
    routes = nested_lookup('route', ipRoutes)
    routeProtocol = nested_lookup('source_protocol', ipRoutes)
    with open (f'Outputs/learned_routes_{device}.txt', 'w') as tempFile:
        for route in routes:
            tempFile.write(str(f'{route} is a {routeProtocol[count]} route\n'))
            counter = len(routeProtocol) - 1
            if count < counter:
                count = count + 1
            else:
                count = 0  
