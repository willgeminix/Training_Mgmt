import datetime
import pandas as pd


class Exercise:

    def __init__(self, intensity_level):
        # intensity_level is how hard the user want to train
        self.__intensity_level = intensity_level
        strength_list = []
        cardio_list = []

    @property
    def intensity_level(self):
        return self.__intensity_level

    @intensity_level.setter
    def intensity_level(self, value):
        self.intensity_level = value
