#!./venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup
from utils.get_from_netbox import netboxget
import csv

tb = load(netboxget())
outputDict= {}

for router in  tb.devices:
    temp = tb.devices[router]
    temp.connect()
    bgpParse = temp.parse('show ip route')
    output = nested_lookup('routes', bgpParse)
#    output2 = {router : output[0]}
#    outputDict.update(output2)

#for spam, eggs in outputDict.items():
#    print (str(spam) + str(eggs['default']['neighbor'].keys()))


#pprint(outputDict)
pprint(output)