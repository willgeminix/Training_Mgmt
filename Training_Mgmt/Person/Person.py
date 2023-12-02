import datetime
import pandas as pd

class Person:
    
    def __init__(self, name, bdate, height, weight, gender, purpose, freq):
        self.__name = name
        self.__bdate = datetime.datetime.strptime(bdate, '%Y/%m/%d')
        self.__height = height
        self.__weight = weight
        self.__gender = gender
        self.__purpose = purpose
        self.__frequency = freq
        
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return (datetime.datetime.now() - self.__bdate).total_seconds()//(365.25*24*60*60)
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        self.__weight = value
        
    @property
    def gender(self):
        return self.__gender
    
    @property
    def purpose(self):
        return self.__purpose
    
    @purpose.setter
    def purpose(self, value):
        self.__purpose = value
        
    @property
    def frequency(self):
        return self.__frequency
    
    @frequency.setter
    def frequency(self, value):
        self.__frequency = value