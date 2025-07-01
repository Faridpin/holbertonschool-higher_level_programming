#!/usr/bin/python3
import pickle
class CustomObject:
    ''' Object '''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
    ''' seriallization '''
        with open(filename, "wb") as file:
            return pickle.dump(data, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as file:
            return pickle.load(
