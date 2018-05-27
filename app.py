# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:41:25 2018

@author: visha
"""
import importlib
from config import ConfigBuilder
from workflow import WorkflowBuilder

class AppBuilder:
    def __init__(self, str):
        print("Inside the AppBuilder constructor")
        self.application = str
        self.configuration = ConfigBuilder(self.application)
        self.workflow = WorkflowBuilder(self.application)        
        self.pipeline = []
        
    def buildPipeline(self):
        print("building workflow pipeline for application :: " + self.application)
        
        self.configuration.buildConfiguration()
        self.workflow.buildWorkflow()
        
        for instance in self.workflow.pipeline:
            print("adding instance to pipeline ::" + instance)
            #print(self.configuration.dictionary[process])
            self.pipeline.append(self.configuration.dictionary[instance])
        

if __name__ == "__main__":
    # Create an object:
    x = AppBuilder("")
    module = importlib.import_module('base.Classification.Classification')
    my_class = getattr(module, 'Classifier')
    my_instance = my_class('base')
    my_method = getattr(my_instance, 'sayHello')
    my_method()
    x.buildPipeline()
    
    
"""    tokenDict = {
    "cat": deal_with_a_cat,
    "dog": deal_with_a_dog,
    "bear": deal_with_a_bear,
    }
"""    
    
    