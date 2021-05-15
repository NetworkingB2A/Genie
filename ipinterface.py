#!./venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup
import csv
from genie.utils import Dq

tb = load('./testbed/testbed.yml')
outputDict= {}

for router in  tb.devices:
    temp = tb.devices[router]
    temp.connect(log_stdout=False)
    output = temp.parse('show cdp neighbors detail')
    tester = output.q.contains('entry_addresses')
    #output = temp.parse('show ip interface')
    pprint(output)
    pprint(tester)