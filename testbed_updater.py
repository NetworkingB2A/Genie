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
    "name": {
        "Router19": {
            "connections": {"cli": {"ip": "192.168.2.19", "protocol": "ssh"}},
            "credentials": {
                "default": {"password": "cisco", "username": "cisco"},
                "enable": {"password": "cisco"},
            },
            "os": "ios",
        }
    }
}
