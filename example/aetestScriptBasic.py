import logging

from pyats import aetest
from genie.testbed import load
from unicon.core.errors import TimeoutError, StateMachineError, ConnectionError

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        '''connect to all your testbed devices'''
        testbed.connect()

class testcase01(aetest.Testcase):
    '''The first testcase'''

    @aetest.test
    def test01(self):
        pass

    @aetest.test
    def test02(self):
        pass

class testcase02(aetest.Testcase):
    '''The second testcase'''
    '''Testcases can have Setup/Cleanup steps to prepare network for testing. EX: perform configuration, start traffic generation'''
    @aetest.setup
    def setup(self):
        pass

    @aetest.test
    def test(self):
        pass

    @aetest.cleanup
    def cleanup(self):
        pass
