# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:41:25 2018

@author: visha
"""
import importlib

class AppBuilder:
    def __init__(self, str):
        print("Inside the AppBuilder constructor")
        self.application = str
    
    

if __name__ == "__main__":
    # Create an object:
    x = AppBuilder("")
    module = importlib.import_module('base.Classification.Classification')
    my_class = getattr(module, 'Classifier')
    my_instance = my_class('base')
    my_method = getattr(my_instance, 'sayHello')
    my_method()
    
    tokenDict = {
    "cat": deal_with_a_cat,
    "dog": deal_with_a_dog,
    "bear": deal_with_a_bear,
    }
    
    
    