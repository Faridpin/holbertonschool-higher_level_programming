#!/usr/bin/python3
''' Basic seriallization '''


import pickle


def serialize_and_save_to_file(data, filename):
    ''' seriallization '''
    with open(filename, "wb") as file:
        return pickle.dump(data, file)


def load_and_deserialize(filename):
    ''' deserialization '''
    with open(filename, "rb") as file:
        return pickle.load(file)
