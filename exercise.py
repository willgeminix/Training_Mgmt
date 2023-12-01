import datetime
import pandas as pd


class Exercise:

    def __init__(self, intensity_level, body_part):
        # intensity_level is how hard the user want to train
        self.__intensity_level = intensity_level
        self.__body_part = body_part
        chest_list = [
            "bench press",
            "incline bench press",
            "dumbell flat bench press",
            "dumbell incline bench press",
            "dip push up",
            "pec deck flys",
            "dumbbell flys",
            "chest press",
            "cable crossover",
            "push-up variations",
            "svend press",
            "guillotine press"
        ]
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
