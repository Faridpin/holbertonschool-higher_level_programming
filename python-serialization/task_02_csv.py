#!/usr/bin/python3
import csv
import json
''' 2 '''


def convert_csv_to_json(csv_filename):
    ''' 2 '''
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
