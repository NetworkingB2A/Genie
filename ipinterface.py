#!./venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup
import csv
from genie.utils import Dq

tb = load("./testbed/testbed.yml")
outputDict = {}

for router in tb.devices:
    temp = tb.devices[router]
    temp.connect()
    # output = temp.learn('vrf')
    # tester = output.q.contains('entry_addresses')
    output2 = temp.parse("show version")
    # print(output)
    print(output2)
