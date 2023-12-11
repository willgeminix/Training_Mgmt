


import unittest
import datetime
import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Training_Mgmt.Person.calculate import bmr, tdee, calorie, nutrition
from Training_Mgmt.Person.Person import Person


class TestCalculate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up TestCalculate class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestCalculate class...")

    def setUp(self):
        self.person_male = Person(
            "Will Xu", "1990-01-01", 180, 70, "Male", "Bulking", "Lightly exercise")
        self.person_female = Person(
            "Alice Zhang", "1985-05-15", 165, 60, "Female", "Cutting", "No exercise")
        self.person_male_1 = Person(
            "Yuyang Peng", "1995-01-01", 190, 80, "Male", "Bulking", "Moderately active")
        self.person_female_1 = Person(
            "Alan Zhang", "2000-05-15", 165, 55, "Female", "Cutting", "Very active")

    def tearDown(self):
        del self.person_male
        del self.person_female

    def test_bmr_type(self):
        calculated_bmr_1 = bmr(self.person_male)
        calculated_bmr_2 = bmr(self.person_male_1)
        calculated_bmr_3 = bmr(self.person_female)
        calculated_bmr_4 = bmr(self.person_female_1)
        self.assertIsInstance(calculated_bmr_1, float)
        self.assertIsInstance(calculated_bmr_2, float)
        self.assertIsInstance(calculated_bmr_3, float)
        self.assertIsInstance(calculated_bmr_4, float)

    def test_bmr(self):
        random.seed(1)
        calculated_bmr_1 = bmr(self.person_male)
        calculated_bmr_2 = bmr(self.person_male_1)
        calculated_bmr_3 = bmr(self.person_female)
        calculated_bmr_4 = bmr(self.person_female_1)
        self.assertEqual(calculated_bmr_1, 1702.63)
        self.assertEqual(calculated_bmr_2, 1912.98)
        self.assertEqual(calculated_bmr_3, 1349.04)
        self.assertEqual(calculated_bmr_4, 1367.76)

    def test_tdee(self):
        random.seed(1)
        calculated_tdee_1 = tdee(self.person_male)
        calculated_tdee_2 = tdee(self.person_male_1)
        calculated_tdee_3 = tdee(self.person_female)
        calculated_tdee_4 = tdee(self.person_female_1)
        self.assertEqual(calculated_tdee_1, 2341.12)
        self.assertEqual(calculated_tdee_2, 2965.12)
        self.assertEqual(calculated_tdee_3, 1618.85)
        self.assertEqual(calculated_tdee_4, 2359.39)

    def test_calorie(self):
        random.seed(1)
        calculated_calorie_1 = calorie(self.person_male)
        calculated_calorie_2 = calorie(self.person_male_1)
        calculated_calorie_3 = calorie(self.person_female)
        calculated_calorie_4 = calorie(self.person_female_1)
        self.assertEqual(calculated_calorie_1, 2625.12)
        self.assertEqual(calculated_calorie_2, 3427.12)
        self.assertEqual(calculated_calorie_3, 1000.85)
        self.assertEqual(calculated_calorie_4, 1487.39)

    def test_nutrition_bulking(self):
        random.seed(1)
        protein_1, carbon_1, fat_1 = nutrition(self.person_male)
        protein_2, carbon_2, fat_2 = nutrition(self.person_male_1)
        protein_3, carbon_3, fat_3 = nutrition(self.person_female)
        protein_4, carbon_4, fat_4 = nutrition(self.person_female_1)

        self.assertTrue(protein_1 > 0 and carbon_1 > 0 and fat_1 > 0)
        self.assertTrue(protein_2 > 0 and carbon_2 > 0 and fat_2 > 0)
        self.assertTrue(protein_3 > 0 and carbon_3 > 0 and fat_3 > 0)
        self.assertTrue(protein_4 > 0 and carbon_4 > 0 and fat_4 > 0)
        self.assertEqual(protein_1, 262.51)
        self.assertEqual(carbon_1, 252.5)
        self.assertEqual(fat_1, 62.79)
        self.assertEqual(protein_2, 340.61)
        self.assertEqual(carbon_2, 277.18)
        self.assertEqual(fat_2, 103.88)
        self.assertEqual(protein_3, 140.86)
        self.assertEqual(carbon_3, 37.38)
        self.assertEqual(fat_3, 17.1)
        self.assertEqual(protein_4, 273.88)
        self.assertEqual(carbon_4, 79.82)
        self.assertEqual(fat_4, 30.07)


if __name__ == '__main__':
    unittest.main()
