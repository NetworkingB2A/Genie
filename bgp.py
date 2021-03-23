#!./venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup
import csv

tb = load('./testbed/testbed.yml')
outputDict= {}

for router in  tb.devices:
    temp = tb.devices[router]
    temp.connect()
    bgpParse = temp.parse('show bgp summary')
    output = nested_lookup('vrf', bgpParse)
    output2 = {router : output[0]}
    outputDict.update(output2)

for spam, eggs in outputDict.items():
    print (str(spam) + str(eggs['default']['neighbor'].keys()))


#pprint(outputDict)
#pprint(bgpParse)