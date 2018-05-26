# -*- coding: utf-8 -*-

class DataCleaner:
    def __init__(self, str):
        print("Inside the DataCleaner constructor")
        self.application = str
    
    def sayHello(self):
        print("Hello World")

if __name__ == "__main__":
    # Create an object:
    x = DataCleaner("")
