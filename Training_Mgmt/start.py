import os
import pandas as pd
import re

from Person import Person, calculate, record



def start():
    name = input("Please enter the user name:")
    try:
        basic_info = pd.read_csv(os.getcwd()+"\\"+name+"_person.csv")
        nutrition_data = pd.read_csv(os.getcwd()+"\\"+name+"_nutrition.csv")
        record_nutrition = record.Record(nutrition_data)
        record_exercise = pd.read_csv(os.getcwd()+"\\"+name+"_exercise.csv")
    except:
        print('The user does NOT exist')
        check = input("Do you want to create the user? ['1' for YES/'q' to quit/any for NO]:")
        if check == '1':
            print('Please create your user.')
            #create the user record file
            basic_info = create()
            basic_info.to_csv(os.getcwd()+"\\"+basic_info['Name'][0]+"_person.csv", index=False)
            #create the nutrition record file
            df_nutrition = pd.DataFrame({'Date':[], 'Calorie':[], 'Protein':[], 'Carbon':[], 'Fat':[]})
            df_nutrition.to_csv(os.getcwd()+"\\"+basic_info['Name'][0]+"_nutrition.csv", index=False)
            #create the exercise record file
            df_exercise = pd.DataFrame({'ss':[]})
            df_exercise.to_csv(os.getcwd()+"\\"+basic_info['Name'][0]+"_exercise.csv", index=False)
            start()
        elif check == 'q':
            print('Thank you for using, see you!')
            return None
        else:
            print("Please try another user name.")
            start()

    person = Person.Person(basic_info["Name"][0], basic_info["Birthdate"][0], basic_info['Height'][0], basic_info['Weight'][0], basic_info['Gender'][0], basic_info['Purpose'][0], basic_info['Frequency'][0])
    
    
    while True:
        print(type(record_nutrition))
        choice_1 = input('What do you want to do:\n[1]: Calculate Nutrition\n[2]: Access the Nutrition Record\n[3]: Exercise Suggestion\n[4]: Access Exercise Record\n[5]: Change Person information\n[6]: Exit\nChoice:')
        if choice_1 not in ['1', '2', '3', '4','5','6']:
            print("Invalid choice, please try again.")
            continue
        elif choice_1 == '6':
            basic_info.to_csv(os.getcwd()+"\\"+str(person.name)+"_person.csv", index=False)
            record_nutrition.to_csv(os.getcwd()+"\\"+str(person.name)+"_nutrition.csv", index=False)
            record_exercise.to_csv(os.getcwd()+"\\"+str(person.name)+"_exercise.csv")
            print("Thank you for using, see you!")
            return None
        elif choice_1 == '1':
            bmr = calculate.bmr(person)
            tdee = calculate.tdee(person)
            calorie = calculate.calorie(person)
            protein, carbon, fat = calculate.nutrition(person)
            print("The nutrition indicators based on your personal information are:\nBMR (Basal Metabolic Rate):{} kcal/day\nTDEE (Total Daily Energy Expenditure): {}kcal/day\nCalorie: {}cal\nProtein: {}g\nCarbon: {}g\nFat: {}g".format(bmr, tdee, calorie, protein, carbon, fat))
            continue
        elif choice_1 == '2':
            while True:
                choice_2 = input("What do you want to with your nutrition record:\n[1]: Add new record\n[2]: Delete existed record\n[3]: Modify the existed record\n[4]: Display the record\n[5]: Return to the previous menu\nChoice:")
                if choice_2 not in ['1', '2', '3', '4','5']:
                    print("Invalid choice, please try again.")
                    continue
                elif choice_2 == '5':
                    break
                elif choice_2 == '1':
                    #input the date, protein, carbon and fat of the newly added record
                    new_date = get_date("Please enter the date of the newly added record: ")
                    protein = get_float_input("Please enter the protein (in g): ")
                    carbon = get_float_input("Please enter the carbon (in g): ")
                    fat = get_float_input("Please enter the fat (in g): ")
                    record_nutrition = record_nutrition.add(new_date, protein, carbon, fat)
                    print(record_nutrition)
                    continue
                elif choice_2 == '3':
                    new_date = get_date("Please enter the date of the newly added record: ")
                    change = input("Which indicators do you want to change?(Calories will be calculated automatically)\n[1]: Protein\n[2]: Carbon\n[3]: Fat\nChoice(For more than one indicators, seperate the number with ','):")
                    change = change.split(',')
                    protein, carbon, fat = '', '', ''
                    for each in change:
                        if each == '1':
                            protein = get_float_input("Please enter the protein (in g): ")
                        elif each == '2':
                            carbon = get_float_input("Please enter the carbon (in g): ")
                        else:
                            fat = get_float_input("Please enter the fat (in g): ")
                    record_nutrition = record_nutrition.modify(new_date, protein, carbon, fat)
                    print(record_nutrition)
                    continue

                elif choice_2 == '4':
                    pass
            continue

def create():
    while True:
        name = input("Please enter the user name:")
        if os.getcwd()+"\\"+name+"_person.csv" in os.listdir():
            print("The user has already existed, please choose another name.")
        elif name == '':
            print("The user name cannot be empty.")
        else:
            break

    bdate = get_date("Please enter the birthdate of the newly added record:")

    while True:
        height = input("Please enter the height (cm):")
        try:
            height = int(height)
            break
        except:
            print("The height should be numeric, please enter again.")

    while True:
        weight = input("Please enter the weight (kg):")
        try:
            weight = int(weight)
            break
        except:
            print("The weight should be numeric, please enter again.")

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
        purpose = input("Please enter the purpose ['1' for bulking, '2' for cutting]:")
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
        freq = input("Please choose the frequecy of exercise.\n['1': No exercise\n'2': 1-2 times per week\n'3': 3-4 times per week\n'4': 5-6 times per week\n'5': more than 6 times per week]\nPlease choose:")
        if freq not in ['1', '2', '3', '4', '5']:
            print('The frequency is NOT correct, please check and try again.')
            continue
        else:
            freq_dict = {'1':'No exercise', '2':'Lightly exercise', '3':'Moderately active', '4':'Very active', '5':'Super active'}
            freq = freq_dict[freq]
            break

    person_data = pd.DataFrame({'Name':[name], 'Birthdate':[bdate], 'Height':[height], 'Weight':[weight], 'Gender':[gender], 'Purpose':[purpose], 'Frequency':[freq]})
    return person_data

def get_float_input(prompt):
    while True:
        value = input(prompt)
        if value.replace(".", "", 1).isdigit():
            return float(value)
        else:
            print("The input should be a valid number. Please check and try again.")

def get_date(prompt):
    while True:
        new_date = input(prompt)
        re_bdate = r'\d{4}/\d{2}/\d{2}'
        if not re.match(re_bdate, new_date):
            print("The date does not follow the required format, please check and try again.")
            continue
        elif new_date[5:7] not in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            print("The MONTH does NOT align with the format, please check and enter again.")
            continue
        elif (not new_date[9:].isnumeric()) or (int(new_date[9:])<=0) or (int(new_date[9:])>31):
            print("The DAY does NOT align with the format, please check and enter again.")
            continue
        else:
            return new_date
        
if __name__ =='__main__':
    start()