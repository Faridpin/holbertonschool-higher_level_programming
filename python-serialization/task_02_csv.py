#!/usr/bin/python3
import csv 
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            with open('data.json', "w", encoding="utf-8") as j:
                json.dump(list(csv.DictReader(f)), j)
        return true
    except Exception:
        return None
