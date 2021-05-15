#! ../venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup



class LearnRoutes:
    def __init__(self, testbedData):
        self.testbedData = testbedData

    def LearningRouting(self):
        tb = load(self.testbedData)

        for device in  tb.devices:
            tempConnect = tb.devices[device]
            tempConnect.connect(log_stdout=False)
            ipRoutes = tempConnect.parse('show ip route ')
        
        
            routes = nested_lookup('routes', ipRoutes)[0]
            with open (f'Outputs/learned_routes_{device}.txt', 'w') as tempFile:
                for (routeTemp, routeFacts) in routes.items():
                    tempFile.write(str(f'{routeTemp} is a { routeFacts["source_protocol"]} route\n'))
    