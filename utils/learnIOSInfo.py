#! ../venv/bin/python
from genie.testbed import load
from pprint import pprint
from nested_lookup import nested_lookup


class LearnIOSInfo:
    def __init__(self, networkDevice, deviceName):
        self.networkDevice = networkDevice
        self.deviceName = deviceName

    def LearningRouting(self):
        tb = self.networkDevice
        hostname = self.deviceName
        ipRoutes = tb.parse("show ip route ")
        routes = nested_lookup("routes", ipRoutes)[0]
        with open(f"Outputs/learned_routes_{hostname}.txt", "w") as tempFile:
            for (routeTemp, routeFacts) in routes.items():
                tempFile.write(
                    str(f'{routeTemp} is a { routeFacts["source_protocol"]} route\n')
                )

    def LearningCDPNeighbors(self):
        tb = self.networkDevice
        hostname = self.deviceName

        cdpNeighbors = tb.parse("show cdp neighbors detail")
        with open(f"Outputs/learned_cdp_neighbors_{hostname}.txt", "w") as tempFile:
            for key, value in cdpNeighbors["index"].items():
                neighborName = nested_lookup("device_id", value)[0]
                try:
                    # this next part is really ugly but it works
                    # might want to revisit
                    ((neighborIPAddress, toss),) = nested_lookup(
                        "management_addresses", value
                    )[0].items()
                except ValueError:
                    neighborIPAddress = "No IP address assigned"
                localInterface = nested_lookup("local_interface", value)[0]
                neighborInterface = nested_lookup("port_id", value)[0]
                tempFile.write(
                    str(
                        f"{hostname} has port {localInterface} connecteed to {neighborName}'s on port {neighborInterface}\n"
                    )
                )
