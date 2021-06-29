#! venv/bin/python

# TODO:create class for this script
# TODO:Add to testbed file


# need to use
# tb.__contains__('Router10')
"""
['CFG_TOPOLOGY_CLASS', 'ENTRY_POINT_NAME', '_Base__instances', '_Base_instances', 
'__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', '_conf_priority', '_convert', '_find_objects', '_find_parent_class', '_to_dict', 
'add_device', 'alias', 'build_config', 'build_unconfig', 'clean', 
'config_on_device', 'config_on_devices', 'connect', 'credentials', 'custom', 
'devices', 'features', 'find_devices', 'find_features', 'find_interfaces', 'find_links', 
'get_build_objects', 'interfaces', 'ipv4_cache', 'ipv6_cache', 'links', 'mac_cache', 'name', 
'object_instances', 'passwords', 'passwords_deprecation_suppress', 'raw_config', 'remove_device', 
'server_cred_deprecation_suppress', 'servers', 'set_active_interfaces', 'squeeze', 'tacacs', 'tacacs_deprecation_suppress', 
'testbed', 'testbed_file']
"""


Router19 = {
        "Router19": {
            "connections": {"cli": {"ip": "192.168.2.19", "protocol": "ssh"}},
            "credentials": {
                "default": {"password": "cisco", "username": "cisco"},
                "enable": {"password": "cisco"},
            },
            "os": "ios",
        }
    }


new_device = topology.Device('Router19')

>>> pprint(tb.__dict__)
{'alias': 'Network defaults',
 'clean': AttrDict({}),
 'credentials': Credentials(NestedAttrDict({'default': NestedAttrDict({'password': ****************, 'username': 'cisco'}), 'enable': NestedAttrDict({'password': ****************})})),
 'custom': AttrDict({}),
 'devices': {'': <Testbed object '' at 0x7fbaaa4000f0>,
             'Router10': <Device Router10 at 0x7fbaca3d1ac8>,
             'Router20': <Device Router20 at 0x7fbaca3ee208>},
 'ipv4_cache': <genie.conf.base.utils.IPv4InterfaceCache object at 0x7fbaca3c2fd0>,
 'ipv6_cache': <genie.conf.base.utils.IPv6InterfaceCache object at 0x7fbaca3d19e8>,
 'mac_cache': <genie.conf.base.utils.MACCache object at 0x7fbaca3d1940>,
 'name': 'Network defaults',
 'passwords': {'enable': 'lab',
               'line': 'lab',
               'linux': 'lab',
               'tacacs': 'lab'},
 'raw_config': {'devices': {'Router10': {'connections': {'cli': {'ip': '192.168.2.10',
                                                                 'protocol': 'ssh'}},
                                         'os': 'ios',
                                         'type': 'ios'},
                            'Router20': {'connections': {'cli': {'ip': '192.168.2.20',
                                                                 'protocol': 'ssh'}},
                                         'os': 'ios',
                                         'type': 'ios'}},
                'testbed': {'credentials': {'default': {'password': 'cisco',
                                                        'username': 'cisco'},
                                            'enable': {'password': 'cisco'}},
                            'name': 'Network defaults',
                            'testbed_file': './testbed/testbed.yml'},
                'topology': {}},
 'servers': AttrDict({}),
 'tacacs': {'login_prompt': 'login:',
            'password_prompt': 'Password:',
            'username': 'angella'},
 'testbed_file': './testbed/testbed.yml'}



Router19 = { 'name': 'Network defaults',
 'passwords': {'enable': 'lab',
               'line': 'lab',
               'linux': 'lab',
               'tacacs': 'lab'},
 'raw_config': {'devices': {'Router10': {'connections': {'cli': {'ip': '192.168.2.10',
                                                                 'protocol': 'ssh'}},
                                         'os': 'ios',
                                         'type': 'ios'}}}}



!!!!! This worked, I can add devices to my testbed !!!!!!!!!!!!!!!!!!!!

>>> from pyats import topology
>>> Router19 = {
...         "Router19": {
...             "connections": 
                  {"cli": 
                    {"ip": "192.168.2.19", 
                    "protocol": "ssh"}},
...               "credentials": {
...                 "default": 
                      {"password": "cisco", 
                       "username": "cisco"},
...                 "enable": 
                      {"password": "cisco"},
...             },
...             "os": "ios",
...         }
...     }
>>> new_device = topology.Device('Router19')
>>> testbed.add_device(new_device)
>>> tb.add_device(new_device)
>>> tb.devices
TopologyDict({'Router10': <Device Router10 at 0x7fbaca3d1ac8>, 'Router20': <Device Router20 at 0x7fbaca3ee208>, '': <Testbed object '' at 0x7fbaaa4000f0>, 'Router19': <Device Router19 at 0x7fbaaa4003c8>})