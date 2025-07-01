#!/usr/bin/python3
import pickle


def serialize_and_save_to_file(data, filename):
    ''' seriallization '''

    with open(filename, "wb") as f:
        return pickle.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
