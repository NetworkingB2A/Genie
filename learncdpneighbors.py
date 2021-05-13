#! venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup
from utils.get_from_netbox import netboxget

tb = load(netboxget())

for device in  tb.devices:
    tempConnect = tb.devices[device]
    tempConnect.connect()
    cdpNeighbors = tempConnect.parse('show cdp neighbors detail')
pprint(cdpNeighbors)