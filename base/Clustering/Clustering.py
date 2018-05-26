# -*- coding: utf-8 -*-

class Cluster:
    def __init__(self, str):
        print("Inside the Cluster constructor")
        self.application = str
    
    def sayHello(self):
        print("Hello World")

if __name__ == "__main__":
    # Create an object:
    x = Cluster("")