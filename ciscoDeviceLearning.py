#!venv/bin/python

from utils.get_from_netbox import netboxget
from utils.learncdpneighbors import LearnCDPNeighbor
from utils.learnRoutes import LearnRoutes


CDP = LearnCDPNeighbor(netboxget())
Routing = LearnRoutes(netboxget())

print('learning routing')
Routing.LearningRouting()
print('learning CDP Neighbors')
CDP.LearningCDPNeighbors()
print('learn complete')