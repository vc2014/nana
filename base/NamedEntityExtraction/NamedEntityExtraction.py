# -*- coding: utf-8 -*-

class NEE:
    def __init__(self, str):
        print("Inside the NEE constructor")
        self.application = str
    
    def sayHello(self):
        print("Hello World")

if __name__ == "__main__":
    # Create an object:
    x = NEE("")