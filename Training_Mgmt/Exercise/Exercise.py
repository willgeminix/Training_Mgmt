import datetime
import pandas as pd
import random


class Exercise():

    def __init__(self, intensity_level, body_part=None):
        self.__intensity_level = intensity_level
        self.__body_part = body_part if body_part is not None else []

        self.chest_exercises = {
            "bench press": "https://www.youtube.com/watch?v=4Y2ZdHCOXok&pp=ygULYmVuY2ggcHJlc3M%3D",
            "incline bench press": "https://www.youtube.com/watch?v=SrqOu55lrYU&pp=ygUTaW5jbGluZSBiZW5jaCBwcmVzcw%3D%3D",
            "dumbell flat bench press": "https://www.youtube.com/watch?v=QsYre__-aro&pp=ygUYZHVtYmVsbCBmbGF0IGJlbmNoIHByZXNz",
            "dumbell incline bench press": "https://www.youtube.com/watch?v=8iPEnn-ltC8&pp=ygUbZHVtYmVsbCBpbmNsaW5lIGJlbmNoIHByZXNz",
            "dip push up": "https://www.youtube.com/watch?v=ybjGSN9IwaA&pp=ygULZGlwIHB1c2ggdXA%3D",
            "pec deck flys": "https://www.youtube.com/shorts/g3T7LsEeDWQ",
            "cable crossover": "https://www.youtube.com/watch?v=taI4XduLpTk&pp=ygUPY2FibGUgY3Jvc3NvdmVy",
        }

        self.shoulder_exercises = {
            "overhead press": "https://www.youtube.com/watch?v=_RlRDWO2jfg&pp=ygUOb3ZlcmhlYWQgcHJlc3M%3D",
            "lateral raise": "https://www.youtube.com/watch?v=3VcKaXpzqRo&t=21s&pp=ygUNbGF0ZXJhbCByYWlzZQ%3D%3D",
            "front raise": "https://www.youtube.com/watch?v=-t7fuZ0KhDA&pp=ygULZnJvbnQgcmFpc2U%3D",
            "rear delt fly": "https://www.youtube.com/watch?v=EA7u4Q_8HQ0&pp=ygUNcmVhciBkZWx0IGZseQ%3D%3D",
            "upright row": "https://www.youtube.com/watch?v=Fq67opsS_hc&pp=ygULdXByaWdodCByb3c%3D",
            "face pull": "https://www.youtube.com/watch?v=ljgqer1ZpXg&pp=ygUJZmFjZSBwdWxs",
            "shrugs": "https://www.youtube.com/watch?v=cJRVVxmytaM&pp=ygUGc2hydWdz"
        }
        self.back_exercises = {
            "pull-ups": "https://www.youtube.com/watch?v=eGo4IYlbE5g&pp=ygUIcHVsbC11cHM%3D",
            "lat pulldown": "https://www.youtube.com/watch?v=SALxEARiMkw&pp=ygUMbGF0IHB1bGxkb3du",
            "bent-over row": "https://www.youtube.com/watch?v=FWJR5Ve8bnQ&pp=ygUNYmVudC1vdmVyIHJvdw%3D%3D",
            "deadlift": "https://www.youtube.com/watch?v=XxWcirHIwVo&pp=ygUIZGVhZGxpZnQ%3D",
            "t-bar row": "https://www.youtube.com/watch?v=j3Igk5nyZE4&pp=ygUJdC1iYXIgcm93",
            "seated cable row": "https://www.youtube.com/watch?v=GZbfZ033f74&pp=ygUQc2VhdGVkIGNhYmxlIHJvdw%3D%3D",
            "single-arm dumbbell row": "https://www.youtube.com/watch?v=roCP6wCXPqo&pp=ygUXc2luZ2xlLWFybSBkdW1iYmVsbCByb3c%3D",
            "back extension": "https://www.youtube.com/watch?v=ph3pddpKzzw&pp=ygUOYmFjayBleHRlbnNpb24%3D"
        }
        self.legs_exercises = {
            "squats": "https://www.youtube.com/shorts/AIZ8q1qruKw",
            "lunges": "https://www.youtube.com/shorts/yXVHr7wrleQ",
            "leg press": "https://www.youtube.com/watch?v=IZxyjW7MPJQ&pp=ygUJbGVnIHByZXNz",
            "leg extension": "https://www.youtube.com/watch?v=ljO4jkwv8wQ&pp=ygUNbGVnIGV4dGVuc2lvbg%3D%3D",
            "leg curl": "https://www.youtube.com/watch?v=ELOCsoDSmrg&pp=ygUIbGVnIGN1cmw%3D",
            "calf raises": "https://www.youtube.com/watch?v=d2GgSoHvIXo&pp=ygULY2FsZiByYWlzZXM%3D",
            "step-ups": "https://www.youtube.com/watch?v=WCFCdxzFBa4&pp=ygUIc3RlcC11cHM%3D",
            "sumo squats": "https://www.youtube.com/watch?v=9ZuXKqRbT9k",
            "box jumps": "https://www.youtube.com/watch?v=hxldG9FX4j4",
            "wall sit": "https://www.youtube.com/watch?v=y-wV4Venusw",
            "glute bridge": "https://www.youtube.com/watch?v=8bbE64NuDTU"
        }
        self.triceps_exercises = {
            "triceps pushdown": "https://www.youtube.com/watch?v=2-LAMcpzODU",
            "overhead triceps extension": "https://www.youtube.com/watch?v=-Vyt2QdsR7E&pp=ygUab3ZlcmhlYWQgdHJpY2VwcyBleHRlbnNpb24%3D",
            "skull crushers": "https://www.youtube.com/watch?v=d_KZxkY_0cM&pp=ygUOc2t1bGwgY3J1c2hlcnM%3D",
            "close grip bench press": "https://www.youtube.com/watch?v=wxVRe9pmJdk&pp=ygUWY2xvc2UgZ3JpcCBiZW5jaCBwcmVzcw%3D%3D",
            "diamond push-ups": "https://www.youtube.com/watch?v=J0DnG1_S92I",
            "triceps kickback": "https://www.youtube.com/watch?v=6SS6K3lAwZ8&pp=ygUQdHJpY2VwcyBraWNrYmFjaw%3D%3D",
            "single-arm triceps extension": "https://www.youtube.com/watch?v=_gsUck-7M74&pp=ygUcc2luZ2xlLWFybSB0cmljZXBzIGV4dGVuc2lvbg%3D%3D",
            "triceps rope pushdown": "https://www.youtube.com/watch?v=kiuVA0gs3EI&pp=ygUVdHJpY2VwcyByb3BlIHB1c2hkb3du",
            "triceps overhead press with dumbbell": "https://www.youtube.com/watch?v=-Vyt2QdsR7E&pp=ygUkdHJpY2VwcyBvdmVyaGVhZCBwcmVzcyB3aXRoIGR1bWJiZWxs",
            "reverse grip pushdown": "https://www.youtube.com/watch?v=o2HRy4ay4rE&pp=ygUVcmV2ZXJzZSBncmlwIHB1c2hkb3du"
        }

        self.biceps_exercises = {
            "bicep curl": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo",
            "hammer curl": "https://www.youtube.com/watch?v=zC3nLlEvin4",
            "preacher curl": "https://www.youtube.com/watch?v=fIWP-FRFNU0",
            "concentration curl": "https://www.youtube.com/watch?v=0AUGkch3tzc",
            "cable curl": "https://www.youtube.com/watch?v=NFzTWp2qpiE&pp=ygUKY2FibGUgY3VybA%3D%3D",
            "reverse curl": "https://www.youtube.com/watch?v=nRgxYX2Ve9w&pp=ygUMcmV2ZXJzZSBjdXJs",
            "incline dumbbell curl": "https://www.youtube.com/watch?v=soxrZlIl35U",
            "barbell curl": "https://www.youtube.com/watch?v=kwG2ipFRgfo",
            "Zottman curl": "https://www.youtube.com/watch?v=-kwe1EOiWMY",
            "alternate dumbbell curl": "https://www.youtube.com/watch?v=sAq_ocpRh_I",
        }

        self.cardio_list = [
            "running",
            "indoor cycling",
            "rowing machine",
            "stair climber machine",
            "elliptical trainer",
            "step mill",
            "assault bike",
            "arc trainer",
        ]

    @property
    def intensity_level(self):
        return self.__intensity_level

    @intensity_level.setter
    def intensity_level(self, value):
        self.__intensity_level = value

    @property
    def body_part(self):
        return self.__body_part

    @body_part.setter
    def body_part(self, value):
        self.__body_part = value

    def strength_suggestion(self):
        exercise_num = 0
        if self.__intensity_level == "easy":
            exercise_num = 5
        elif self.__intensity_level == "medium":
            exercise_num = 6
        elif self.__intensity_level == "hard":
            exercise_num = 7

        if isinstance(self.__body_part, list):
            return (self.strength_choices_helper(exercise_num))
        else:
            return "Error, have to do a list"

    def cardio_suggestion(self):
        exercise_min = 0
        if self.__intensity_level == "easy":
            exercise_min = 30
        elif self.__intensity_level == "medium":
            exercise_min = 40
        elif self.__intensity_level == "hard":
            exercise_min = 60

        random_exercise = random.choice(self.cardio_list)  # 随机选择一个运动
        return {random_exercise: exercise_min}

    def hybrid_suggestion(self):
        exercise_num = 0
        exercise_min = 0
        if self.__intensity_level == "easy":
            exercise_num = 3
            exercise_min = 15
        elif self.__intensity_level == "medium":
            exercise_num = 4
            exercise_min = 30
        elif self.__intensity_level == "hard":
            exercise_num = 5
            exercise_min = 40
        stength_choices = self.strength_choices_helper(exercise_num)
        random_cardio_exercise = random.choice(self.cardio_list)  # 随机选择一个运动
        return [stength_choices, {random_cardio_exercise: exercise_min}]

    def strength_choices_helper(self, exercise_num):
        exercises_per_part = exercise_num // len(self.__body_part)
        remaining_exercises = exercise_num % len(self.__body_part)
        random_exercises = {}

        for part in self.__body_part:
            allocated_exercises = exercises_per_part
            if remaining_exercises > 0:
                allocated_exercises += 1
                remaining_exercises -= 1

            if part == "chest":
                random_keys = random.sample(
                    list(self.chest_exercises.keys()), allocated_exercises)
                random_exercises.update(
                    {key: self.chest_exercises[key] for key in random_keys})
            elif part == "shoulder":
                random_keys = random.sample(
                    list(self.shoulder_exercises.keys()), allocated_exercises)
                random_exercises.update(
                    {key: self.shoulder_exercises[key] for key in random_keys})
            elif part == "back":
                random_keys = random.sample(
                    list(self.back_exercises.keys()), allocated_exercises)
                random_exercises.update(
                    {key: self.back_exercises[key] for key in random_keys})
            elif part == "leg":
                random_keys = random.sample(
                    list(self.legs_exercises.keys()), allocated_exercises)
                random_exercises.update(
                    {key: self.legs_exercises[key] for key in random_keys})
            elif part == "bicep":
                random_keys = random.sample(
                    list(self.biceps_exercises.keys()), allocated_exercises)
                random_exercises.update(
                    {key: self.biceps_exercises[key] for key in random_keys})
            elif part == "tricep":
                random_keys = random.sample(
                    list(self.triceps_exercises.keys()), allocated_exercises)
                random_exercises.update(
                    {key: self.triceps_exercises[key] for key in random_keys})

        return random_exercises


# exercise = Exercise("hard", ["chest"])
# print(exercise.strength_suggestion())
# print(exercise.cardio_suggestion())
# print(exercise.hybrid_suggestion())
