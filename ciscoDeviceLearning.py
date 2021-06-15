#!venv/bin/python

from utils.get_from_netbox import netboxget
from utils.learnIOSInfo import LearnIOSInfo
from genie.testbed import load

tb = load(netboxget())

print("starting learns")
deviceCount = len(tb.devices)
print("Number of devices to learn: " + str(deviceCount))

for device in tb.devices:
    tempConnect = tb.devices[device]
    tempConnect.connect(init_exec_commands=[], init_config_commands=[],log_stdout=False)
    networkObject = LearnIOSInfo(tempConnect, device)
    print(f"Current Number of devices to learn: {str(LearnIOSInfo.testbedDeviceCount)} / { str(deviceCount)} ")
    networkObject.LearningRouting()
    networkObject.LearningCDPNeighbors()

print("learn complete")
