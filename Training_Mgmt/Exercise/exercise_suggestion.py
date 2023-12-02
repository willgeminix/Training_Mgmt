import Exercise.exercise_suggestion
import random
exercise = exercise.Exercise("easy", "chest")


def strength_suggestion():
    random.sample(exercise.chest_list, 6)


def cardio_suggestion():
    random.sample(exercise.cardio_list, 6)
