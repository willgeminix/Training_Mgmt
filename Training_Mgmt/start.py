import os
import pandas as pd
import re

from Person import Person, calculate, record
from Exercise import Record as Exercise_Record


def start():

    try:
        name = input("Please enter the user name:")
        basic_info = pd.read_csv(name+"_person.csv")
        person = Person.Person(basic_info["Name"][0], basic_info["Birthdate"][0], basic_info['Height'][0],
                               basic_info['Weight'][0], basic_info['Gender'][0], basic_info['Purpose'][0], basic_info['Frequency'][0])
        nutrition_data = pd.read_csv(name+"_nutrition.csv")
        record_nutrition = record.Record(nutrition_data)
        exercise_record = Exercise_Record.Record(person)
        record_exercise = pd.read_csv(name+"_exercise.csv")
    except:
        print('The user does NOT exist')
        check = input(
            "Do you want to create the user? ['1' for YES/'q' to quit/any for NO]:")
        if check == '1':
            print('Please create your user.')
            # create the user record file
            basic_info = create()
            basic_info.to_csv(basic_info['Name'][0]+"_person.csv", index=False)
            # create the nutrition record file
            df_nutrition = pd.DataFrame(
                {'Date': [], 'Calorie': [], 'Protein': [], 'Carbon': [], 'Fat': []})
            df_nutrition.to_csv(
                basic_info['Name'][0]+"_nutrition.csv", index=False)
            # create the exercise record file
            df_exercise = pd.DataFrame({'index': [], 'date': [], 'exercise_name': [
            ], 'exercise_set': [], 'exercise_rep': []})
            df_exercise.to_csv(basic_info['Name']
                               [0]+"_exercise.csv", index=False)
            start()
        elif check == 'q':
            print('Thank you for using, see you!')
            return None
        else:
            print("Please try another user name.")
            start()

    while True:
        choice_1 = input(
            'What do you want to do:\n[1]: Calculate Nutrition\n[2]: Access the Nutrition Record\n[3]: Exercise Suggestion\n[4]: Manipulate Exercise Record\n[5]: Change Person information\n[6]: Exit\nChoice:')
        if choice_1 not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice, please try again.")
            continue
        elif choice_1 == '6':
            basic_info.to_csv(str(person.name)+"_person.csv", index=False)
            record_nutrition.to_csv(
                str(person.name)+"_nutrition.csv", index=False)
            record_exercise.to_csv(str(person.name)+"_exercise.csv")
            print("Thank you for using, see you!")
            return
        elif choice_1 == '1':
            bmr = calculate.bmr(person)
            tdee = calculate.tdee(person)
            calorie = calculate.calorie(person)
            protein, carbon, fat = calculate.nutrition(person)
            print("The nutrition indicators based on your personal information are:\nBMR (Basal Metabolic Rate):{} kcal/day\nTDEE (Total Daily Energy Expenditure): {}kcal/day\nCalorie: {}cal\nProtein: {}g\nCarbon: {}g\nFat: {}g".format(bmr, tdee, calorie, protein, carbon, fat))
            continue
        elif choice_1 == '2':
            while True:
                choice_2 = input(
                    "What do you want to with your nutrition record:\n[1]: Add new record\n[2]: Delete existed record\n[3]: Modify the existed record\n[4]: Display the record\n[5]: Return to the previous menu\nChoice:")
                if choice_2 not in ['1', '2', '3', '4', '5']:
                    print("Invalid choice, please try again.")
                    continue
                elif choice_2 == '5':
                    break
                elif choice_2 == '1':
                    # input the date, protein, carbon and fat of the newly added record
                    new_date = get_date(
                        "Please enter the date of the newly added record: ")
                    protein = get_float_input(
                        "Please enter the protein (in g): ")
                    carbon = get_float_input(
                        "Please enter the carbon (in g): ")
                    fat = get_float_input("Please enter the fat (in g): ")
                    record_nutrition = record_nutrition.add(
                        new_date, protein, carbon, fat)
                    continue
                elif choice_2 == '2':
                    new_date = get_date(
                        "Please enter the date of the record to modify: ")
                    record_nutrition = record_nutrition.remove(new_date)
                    continue
                elif choice_2 == '3':
                    new_date = get_date(
                        "Please enter the date of the record to modify: ")
                    change = input(
                        "Which indicators do you want to change?(Calories will be calculated automatically)\n[1]: Protein\n[2]: Carbon\n[3]: Fat\nFor more than one indicators, seperate the number with ','\nChoice:")
                    change = change.split(',')
                    protein, carbon, fat = '', '', ''
                    for each in change:
                        if each == '1':
                            protein = get_float_input(
                                "Please enter the protein (in g): ")
                        elif each == '2':
                            carbon = get_float_input(
                                "Please enter the carbon (in g): ")
                        else:
                            fat = get_float_input(
                                "Please enter the fat (in g): ")
                    record_nutrition = record_nutrition.modify(
                        new_date, protein, carbon, fat)
                    continue
                elif choice_2 == '4':
                    start_date = get_date("Please enter the start date: ")
                    end_date = get_date("Please enter the end date: ")
                    record_nutrition.show(start_date, end_date)
                    continue
            continue
        # exercise part, recording
        elif choice_1 == '4':
            while True:
                choice_2 = input(
                    "What do you want to do with your exercise record:\n[1]: Add new record\n[2]: Delete existed record\n[3]: Modify the existed record\n[4]: Display the record\n[5]: Return to the previous menu\nChoice:")
                if choice_2 not in ['1', '2', '3', '4', '5']:
                    print("Invalid choice, please try again.")
                    continue
                # return to the previous menu
                elif choice_2 == '5':
                    break
                # add exercise record
                elif choice_2 == '1':
                    add_lst = []
                    exercise_record.test()
                    new_date = get_date(
                        "Please enter the date of the exercise: ")
                    exercise_name = input(
                        "Please enter the name of the exercise: ")
                    exercise_set = input(
                        "Please enter the number of the sets: ")
                    exercise_rep = input(
                        "Please enter the number of the reps: ")
                    add_lst.append({"date": new_date, "exercise_name": exercise_name,
                                    "exercise_set": exercise_set, "exercise_rep": exercise_rep})
                    exercise_record.add(add_lst)
                    continue
                # delete an exercise record
                elif choice_2 == '2':
                    index = get_int_input(
                        "Please enter the index of entry you want to remove: ")
                    exercise_record.remove_by_index(index)
                    continue
                # modify an exercise record
                elif choice_2 == '3':
                    modify_index = get_int_input(
                        "Please enter the index you want to modify: ")
                    new_date = get_date("Please enter the new date: ")
                    new_exercise_name = input(
                        "Please enter the new exercise name: ")
                    new_exercise_sets = get_int_input(
                        "Please enter the new exercise sets: ")
                    new_exercise_reps = get_int_input(
                        "Please enter the new exercise reps: ")

                    exercise_record.modify(modify_index, {"date": new_date,
                                           "exercise_name": new_exercise_name, "exercise_set": new_exercise_sets, "exercise_rep": new_exercise_reps})
                    continue
                # display
                elif choice_2 == '4':
                    exercise_record.display()
                    continue
            continue
        # exercise part, suggestion
        elif choice_1 == '3':
            intensity_level_choice = input(
                "Please choose the intensity level:\n[1]: easy\n[2]: medium\n[3]: hard\nChoice: ")
            if intensity_level_choice not in ['1', '2', '3']:
                print("Invalid choice, please try again.")
                continue
            else:
                intensity_dict = {'1': 'easy', '2': 'medium',
                                  '3': 'hard'}
                intensity_level_choice = intensity_dict[intensity_level_choice]
            type_of_exericise_choice = input(
                "What kind of sports suggestion do you want to ask:\n[1]: Strength\n[2]: Cardio\n[3]: Hybrid\nChoice: ")
            if type_of_exericise_choice not in ['1', '2', '3']:
                print("Invalid choice, please try again.")
                continue

            # strength suggestion
            elif type_of_exericise_choice == '1':
                while True:
                    body_parts = input(
                        "Please choose the body part(s):\n[1]: Chest\n[2]: Shoulder\n[3]: Back\n[4]: Legs\n[5]: Triceps\n[6]: Biceps\nIf you want to train multiple body parts, use ',' to separate, e.g. 1,2,3\nHowever, note that you can't choose more than 3 parts at once, it would be an inappropriate training way\nChoice: ")
                    body_part_lst = body_parts.split(',')
                    if len(body_part_lst) > 3:
                        print(
                            "You can't choose more than 3 body parts! Please try again.")
                        continue
                    for element in body_part_lst:
                        # verify if input is number
                        if element.strip().isdigit():
                            num = int(element.strip())
                            if num < 1 or num > 6:
                                print(
                                    f"Invalid entry: {element}. Please enter a number between 1 and 6. Please try again")
                                continue
                            break
                        else:
                            print(
                                f"Invalid entry: {element}. Please enter the number")
                            continue

            # cardio suggestion
            elif type_of_exericise_choice == '2':
                print("cardio suggestion")
            # hybrid suggestion
            elif type_of_exericise_choice == '3':
                print("hybrid suggestion")


def create():
    while True:
        name = input("Please enter the user name:")
        if name+"_person.csv" in os.listdir():
            print("The user has already existed, please choose another name.")
        elif name == '':
            print("The user name cannot be empty.")
        else:
            break

    bdate = get_date(
        "Please enter the birthdate of the newly added record (YYYY-MM-DD):")

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
        purpose = input(
            "Please enter the purpose [1] for bulking\n[2] for cutting]:")
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
        freq = input(
            "Please choose the frequecy of exercise.\n[1]: No exercise\n[2]: 1-2 times per week\n[3]: 3-4 times per week\n[4]: 5-6 times per week\n[5]: more than 6 times per week\nPlease choose:")
        if freq not in ['1', '2', '3', '4', '5']:
            print('The frequency is NOT correct, please check and try again.')
            continue
        else:
            freq_dict = {'1': 'No exercise', '2': 'Lightly exercise',
                         '3': 'Moderately active', '4': 'Very active', '5': 'Super active'}
            freq = freq_dict[freq]
            break

    person_data = pd.DataFrame({'Name': [name], 'Birthdate': [bdate], 'Height': [height], 'Weight': [
                               weight], 'Gender': [gender], 'Purpose': [purpose], 'Frequency': [freq]})
    return person_data


def get_int_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            return int(value)
        else:
            print("The input should be a valid integer. Please check and try again.")


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
        re_bdate = r'\d{4}-\d{2}-\d{2}'
        if not re.match(re_bdate, new_date):
            print(
                "The date does not follow the required format, please check and try again.")
            continue
        elif new_date[5:7] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            print(
                "The MONTH does NOT align with the format, please check and enter again.")
            continue
        elif (not new_date[8:].isnumeric()) or (int(new_date[8:]) <= 0) or (int(new_date[8:]) > 31):
            print("The DAY does NOT align with the format, please check and enter again.")
            continue
        else:
            return new_date


if __name__ == '__main__':
    start()
