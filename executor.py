# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:41:46 2018

@author: visha
"""

from app import AppBuilder

class ExecutorBuilder:
    def __init__(self, str):
        print("Inside the ExecutorBuilder constructor")
        self.application = str
        self.app = AppBuilder(self.application)
        
    def executePipeline(self):
        
        self.app.buildPipeline()
        
        print("executing workflow pipeline for application :: " + self.application)
        
        for process in self.app.pipeline:
            print("executing process in pipeline ::" + str(process))
            process.sayHello()
        

if __name__ == "__main__":
    # Create an object:
    x = ExecutorBuilder("")
    x.executePipeline()
    