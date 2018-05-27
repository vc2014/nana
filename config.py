# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:40:26 2018

@author: visha
"""

import os

from configparser import ConfigParser
import importlib

class ConfigBuilder:
    def __init__(self, str):
        print("Inside the ConfigBuilder constructor")
        self.application = str
        self.dictionary = {}
    # Two methods:
    def show(self):
        print(self.application)
    
    def showMsg(self, msg):
        print(msg + ':', self.show()) # Calling another method
    
    def getConfiguration(self):
        config_parser = ConfigParser()
        print("loading configuration for application ::" + self.application)            
        try:
            if(os.path.exists(self.application)):
                config_parser.read(self.application + '/config.ini')
            else:
                config_parser.read('config.ini')
        except Exception as ex:
            print(ex)
        
        return config_parser
            
    def buildConfiguration(self):
        
        config_parser = self.getConfiguration()
        for section_name in config_parser.sections():
            print('Section:', section_name)
            print('  Options:', config_parser.options(section_name))
            module=[]
            classes=[]
            for key, value in config_parser.items(section_name):
                print('{} = {}'.format(key, value))
                if(key=='pkg'):
                    packages = value.split(",")
                    i=0
                    for val in packages:
                        print(val)
                        module.insert(len(module), importlib.import_module(val))
                        i=i+1
                else:
                    values = value.split(",")
                    j=0
                    for val in values:
                        classes.insert(len(classes), getattr(module[j], val))
                        #instances.insert(len(instances), classes[j]('base'))
                        #self.dictionary[val] = getattr(module[j], val)
                        self.dictionary[val] = getattr(module[j], val)('base')
                        j=j+1
                    
                    
            print()
            
    def showConfiguration(self):
        
        config_parser = self.getConfiguration()
        for section_name in config_parser.sections():
            print('Section:', section_name)
            print('  Options:', config_parser.options(section_name))
            for key, value in config_parser.items(section_name):
                print('{} = {}'.format(key, value))
            print()
            

if __name__ == "__main__":
    # Create an object:
    x = ConfigBuilder("")
    x.show()
    x.showMsg("A message")
    x.showConfiguration()
    x.buildConfiguration()
    instance = x.dictionary.get('Cluster')('base')
    instance.sayHello()
    