#!venv/bin/python

from utils.get_from_netbox import netboxget
from utils.learnIOSInfo import LearnIOSInfo
from genie.testbed import load


# CDP = LearnCDPNeighbor(netboxget())
# git test


tb = load(netboxget())

print("starting learns")
for device in tb.devices:
    tempConnect = tb.devices[device]
    tempConnect.connect(log_stdout=False)
    networkObject = LearnIOSInfo(tempConnect, device)
    networkObject.LearningRouting()
    networkObject.LearningCDPNeighbors()


# print('learning CDP Neighbors')
# CDP.LearningCDPNeighbors()
print("learn complete")
