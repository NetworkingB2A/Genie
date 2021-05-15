#! ../venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup
from utils.get_from_netbox import netboxget


class LearnCDPNeighbor:
    def __init__(self, testbedData):
        self.testbedData = testbedData
    
    def LearningCDPNeighbors(self):
        tb = load(self.testbedData)
    
        for device in  tb.devices:
            tempConnect = tb.devices[device]
            tempConnect.connect(log_stdout=False)
            cdpNeighbors = tempConnect.parse('show cdp neighbors detail')
            with open (f'Outputs/learned_cdp_neighbors_{device}.txt', 'w') as tempFile:
                for key, value in cdpNeighbors['index'].items():
                    neighborName = nested_lookup('device_id', value)[0]
                    try:
                        #this next part is really ugly but it works
                        #might want to revisit
                        (neighborIPAddress, toss), = nested_lookup('management_addresses', value)[0].items()
                    except ValueError:
                        neighborIPAddress = 'No IP address assigned'
                    localInterface = nested_lookup('local_interface', value)[0]
                    neighborInterface = nested_lookup('port_id', value)[0]           
                    tempFile.write(str(f'{device} has port {localInterface} connecteed to {neighborName}\'s on port {neighborInterface}\n'))
            



    