import datetime
import pandas as pd
import random


class Exercise:

    def __init__(self, intensity_level, body_part):
        # intensity_level is how hard the user want to train
        self.__intensity_level = intensity_level
        self.__body_part = body_part
        self.chest_exercises = {
            "bench press": "https://www.youtube.com/watch?v=4Y2ZdHCOXok&pp=ygULYmVuY2ggcHJlc3M%3D",
            "incline bench press": "https://www.youtube.com/watch?v=SrqOu55lrYU&pp=ygUTaW5jbGluZSBiZW5jaCBwcmVzcw%3D%3D",
            "dumbell flat bench press": "https://www.youtube.com/watch?v=QsYre__-aro&pp=ygUYZHVtYmVsbCBmbGF0IGJlbmNoIHByZXNz",
            "dumbell incline bench press": "https://www.youtube.com/watch?v=8iPEnn-ltC8&pp=ygUbZHVtYmVsbCBpbmNsaW5lIGJlbmNoIHByZXNz",
            "dip push up": "https://www.youtube.com/watch?v=ybjGSN9IwaA&pp=ygULZGlwIHB1c2ggdXA%3D",
            "pec deck flys": "https://www.youtube.com/shorts/g3T7LsEeDWQ",
            "cable crossover": "https://www.youtube.com/watch?v=taI4XduLpTk&pp=ygUPY2FibGUgY3Jvc3NvdmVy",
        }

        shoulder_list = [
            "overhead press",
            "lateral raise",
            "front raise",
            "rear delt fly",
            "arnold press",
            "upright row",
            "face pull",
            "shrugs"
        ]
        back_list = [
            "pull-ups",
            "lat pulldown",
            "bent-over row",
            "deadlift",
            "t-bar row",
            "seated cable row",
            "single-arm dumbbell row",
            "back extension"
        ]
        leg_list = [
            "squats",
            "lunges",
            "deadlifts",
            "leg press",
            "leg extension",
            "leg curl",
            "calf raises",
            "step-ups"
        ]
        triceps_list = [
            "triceps pushdown",
            "overhead triceps extension",
            "skull crushers",
            "close grip bench press",
            "dips",
            "diamond push-ups",
            "triceps kickback",
            "single-arm triceps extension"
        ]
        biceps_list = [
            "bicep curl",
            "hammer curl",
            "preacher curl",
            "concentration curl",
            "cable curl",
            "chin-up",
            "reverse curl",
            "incline dumbbell curl"
        ]
        cardio_list = [
            "treadmill running or walking",
            "indoor cycling on stationary bike",
            "rowing machine",
            "stair climber machine",
            "elliptical trainer",
            "group fitness classes (e.g., Zumba, spinning, aerobics)",
            "step mill",
            "assault bike",
            "arc trainer",
            "versa climber"
        ]

    @property
    def intensity_level(self):
        return self.__intensity_level

    @intensity_level.setter
    def intensity_level(self, value):
        self.intensity_level = value

    @property
    def body_part(self):
        return self.__body_part

    @body_part.setter
    def __body_part(self, value):
        self.__body_part = value

    def strength_suggestion(self):
        if self.__intensity_level == "easy":
            random_keys = random.sample(list(chest_exercises.keys()), 3)
            random_exercises = {
                key: chest_exercises[key] for key in random_keys}
        print(random_exercises)
