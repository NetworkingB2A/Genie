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
    output = temp.parse('show ip interface')
    pprint(output)