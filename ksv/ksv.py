# -*- coding: utf-8 -*-

"""Main module."""

import base64
from collections import OrderedDict
import sys
import yaml

# https://stackoverflow.com/questions/16782112/can-pyyaml-dump-dict-items-in-non-alphabetical-order
def represent_ordereddict(dumper, data):
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


def show_yaml(fin, encode):
    yaml.add_representer(dict, represent_ordereddict)
    y = yaml.safe_load(fin)
    if 'data' not in y:
        sys.exit('File does not appear to be a valid secrets file.')
    data_node = y['data']
    for k in data_node:
        v = data_node[k]
        if encode:
            new_v = base64.b64encode(str.encode(v)).decode()
            data_node[k] = new_v
        else:
            new_v = base64.b64decode(v).decode()
            data_node[k] = new_v
    print(yaml.dump(y, default_flow_style=False))
