#!venv/bin/python

from utils.get_from_netbox import netboxget
from utils.learnIOSInfo import LearnIOSInfo
from genie.testbed import load

tb = load(netboxget())

print("starting learns")
for device in tb.devices:
    tempConnect = tb.devices[device]
    tempConnect.connect(log_stdout=True)
    networkObject = LearnIOSInfo(tempConnect, device)
    networkObject.LearningRouting()
    networkObject.LearningCDPNeighbors()
print("learn complete")
