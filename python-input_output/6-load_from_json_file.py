#!/usr/bin/python3
''' json '''


import json


def load_from_json_file(filename):
    ''' func '''
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
