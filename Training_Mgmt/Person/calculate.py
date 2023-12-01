import random


def bmr(person):
    if person.gender == "Male":
        bmr = 88.362 + (13.397*person.weight) + (4.799*person.height) - (5.677*person.age)
    else:
        bmr = 447.593 + (9.247*person.weight) + (3.098*person.height) - (4.330*person.age)
    
    return round(bmr,2)


def tdee(person):

    bmr = bmr(person)

    active_factor = {"No exercise": 1.2, "Lightly exercise": 1.375, "Moderately active": 1.55, "Very active": 1.725, "Super active":1.9}    
    tdee = bmr * active_factor[person.frequency]

    return round(tdee,2)


def calorie(person):

    calorie = tdee(person)

    if person.purposr == "Bulking":
        calorie = tdee + round(random.uniform(250, 500))
    else:
        calorie = tdee + round(random.uniform(-1000, -500))

    return round(calorie,2)


def nutrition(person):

    calorie = calorie(person)

    if person.purpose == "Bulking":
        protein = calorie * 0.4
        carbon = calorie * random.uniform(0.3, 0.4)
        fat = calorie - protein - carbon
        
    else:
        protein = calorie * 0.65
        carbon = calorie * random.uniform(0.15, 0.2)
        fat = calorie - protein - carbon

    # change the unit of each nutrition to gram
    protein = protein / 4
    carbon = carbon / 4
    fat = fat / 9

    return round(protein,2), round(carbon,2), round(fat,2)