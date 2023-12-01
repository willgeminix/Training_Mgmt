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
        print('The user does NOT exist')
        check = input("Do you want to create the user? ['1' for YES/'q' to quit/any for NO]:")
        if check == 1:
            print('Please create your user.')
            #create the user record file
            person_data = create()
            person_data.to_csv(os.getcwd()+"\\"+person_data['Name'][0]+"_person.csv", index=False)
            #create the nutrition record file
            df_nutrition = pd.DataFrame({'Date':[], 'Calorie':[], 'Protein':[], 'Carbon':[], 'Fat':[]})
            df_nutrition.to_csv(os.getcwd()+"\\"+person_data['Name'][0]+"_nutrition.csv", index=False)
            #create the exercise record file
            df_exercise = pd.DataFrame()
            df_exercise.to_csv(os.getcwd()+"\\"+person_data['Name'][0]+"_exercise.csv", index=False)
            start()
        elif check == 'q':
            print('Thank you for using, see you!')
            return None
        else:
            print("Please try another unser name.")
            start()

    person = Person.Person(basic_info["Name"], basic_info["Birthdate"], basic_info['Height'], basic_info['Weight'], basic_info['Gender'], basic_info['Purpose'], basic_info['Frequncy'])


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

    while True:
        gender = input("Please enter the gender['F'/'M']:")
        if gender not in ["F", "M"]:
            print("The gender is NOT correct, please check and try again.")
            continue
        elif gender == "F":
            gender = "Female"
            break
        else:
            gender = "Male"
            break

    while True:
        purpose = input("Please enter the purpose ['1' for bulking, '2' for cutting]"):
        if purpose not in ['1', '2']:
            print("The purpose is NOT correct, please check and try again.")
            continue
        elif purpose == '1':
            purpose = 'Bulking'
            break
        else:
            purpose = 'Cutting'
            break

    while True:
        freq = input("Please enter the frequecy of exercise.\n'1': No exercise\n'2': 1-2 times per week\n'3': 3-4 times per week\n'4': 5-6 times per week\n'5': more than 6 times per week")
        if freq not in ['1', '2', '3', '4', '5']:
            print('The frequency is NOT correct, please check and try again.')
            continue
        else:
            freq_dict = {'1':'No exercise', '2':'Lightly exercise', '3':'Moderately active', '4':'Very active', '5':'Super active'}
            freq = freq_dict[freq]
            break

    person_data = pd.DataFrame({'Name':[name], 'Birthdate':[bdate], 'Height':[height], 'Weight':[weight], 'Gender':[gender], 'Purpose':[purpose], 'Frequency':[freq]})
    return person_data