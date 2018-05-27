#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:06:21 2018

@author: vishu
"""

import os

from configparser import ConfigParser

class WorkflowBuilder:
    def __init__(self, str):
        print("Inside the WorkflowBuilder constructor")
        self.application = str
        self.pipeline = []
    # Two methods:
    def show(self):
        print(self.application)
    
    def showMsg(self, msg):
        print(msg + ':', self.show()) # Calling another method
    
    def getWorkflow(self):
        config_parser = ConfigParser()
        print("loading workflow.ini for application ::" + self.application)            
        try:
            if(os.path.exists(self.application)):
                config_parser.read(self.application + '/workflow.ini')
            else:
                config_parser.read('workflow.ini')
        except Exception as ex:
            print(ex)
        
        return config_parser
            
    def buildWorkflow(self):
        print("building workflow for application ::" + self.application)
        config_parser = self.getWorkflow()
        for section_name in config_parser.sections():
            print('Section:', section_name)
            print('  Options:', config_parser.options(section_name))
            for key, value in config_parser.items(section_name):
                print('{} = {}'.format(key, value))
                if(key=='primary'):
                    self.pipeline.append(value)
                elif(key=='secondary'):
                    for val in value.split(","):
                        self.pipeline.append(val)
                else:
                    print("not for building pipeline")
                    
        print(self.pipeline)


if __name__ == "__main__":
    # Create an object:
    x = WorkflowBuilder("")
    x.show()
    x.showMsg("A message")
    x.buildWorkflow()
    
    