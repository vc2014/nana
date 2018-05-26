# -*- coding: utf-8 -*-

class Classifier:
    def __init__(self, str):
        print("Inside the Classifier constructor")
        self.application = str
    
    def sayHello(self):
        print("Hello World")

if __name__ == "__main__":
    # Create an object:
    x = Classifier("")
   