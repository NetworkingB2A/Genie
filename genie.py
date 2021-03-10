#!./venv/bin/python3 
from genie.testbed import load
from pprint import pprint

tb = load('./testbed/testbed.yml')

device = tb.devices['R11']

device.connect()

output = device.parse('show bgp summary')

pprint(output)