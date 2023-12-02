import os
import pandas as pd

name = 'Will'
print(os.getcwd()+"\\"+name+"_person.csv")
basic_info = pd.read_csv(os.getcwd()+"\\"+name+"_person.csv", header=True)
print(basic_info)