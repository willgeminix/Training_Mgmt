import os
import pandas as pd

from Person import Person

def start():
    name = input("Please enter the user name:")
    try:
        basic_info = pd.read_csv(os.getcwd()+"\\"+name+"_person.csv", header=True)
        record_nutrition = pd.read_csv(os.getcwd()+"\\"+name+"_nutrition.csv", header=True)
        record_exercise = pd.read_csv(os.getcwd()+"\\"+name+"_exercise.csv", header=True)
    except:
        print('The user does NOT exist. Please create the user first and restart.')
        create()
    person = Person.Person(basic_info["name"], basic_info["bdate"], basic_info['height'], basic_info['weight'], basic_info['gender'], basic_info['purpose'])


def create():
    while True:
        name = input("Please enter the user name:")
        if os.getcwd()+"\\"+name+"_person.csv" in os.listdir():
            print("The user has already existed, please choose another name")
        elif name == '':
            print("The user name cannot be empty.")
        else:
            break

    while True:
        bdate = input("Please enter the birthdate ('YYYY/MM/DD'):")
        try:
            bdate = bdate.split("/")
        except:
            print("The birthdate does NOT align with the format, please check and enter again.")
            continue

        if len(bdate) != 3:
            print("The format of birthdate does NOT align with the format, please check and enter again.")
            continue
        elif (not bdate[0].isnumeric()) or len(bdate[0]) != 4:
            print("The YEAR does NOT align with the format, please check and enter again.")
            continue
        elif bdate[1] not in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            print("The MONTH does NOT align with the format, please check and enter again.")
            continue
        elif (not bdate[2].isnumeric()) or (int(bdate[2])<=0) or (bdate[2]>31):
            print("The DAY does NOT align with the format, please check and enter again.")
            continue
        else:
            break

    while True:
        height = input("Please enter the height (cm):")
        try:
            height = int(height)
            break
        except:
            print("The height should be numeric, please enter again")

    while True:
        weight = input("Please enter the weight (kg):")
        try:
            weight = int(weight)
            break
        except:
            print("The weight should be numeric, please enter again")