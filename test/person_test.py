import unittest
import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Training_Mgmt.Person.Person import Person

class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up TestPerson class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestPerson class...")

    def setUp(self):
        self.person_1 = Person("Will Xu", "1990-01-01", 160, 90, "Male", "Bulking", "No exercise")
        self.person_2 = Person("Yuyang Peng", "1990-01-01", 170, 70, "Male", "Cutting", "Lightly exercise")
        self.person_3 = Person("Alan Zhang", "1990-01-01", 180, 70, "Male", "Cutting", "Very active")
        self.person_4 = Person("Bingshen Yang", "1990-01-01", 190, 80, "Male", "Bulking", "Super active")

    def tearDown(self):
        del self.person_1
        del self.person_2
        del self.person_3
        del self.person_4

    def test_name(self):
        self.assertEqual(self.person_1.name, "Will Xu")
        self.assertEqual(self.person_2.name, "Yuyang Peng")
        self.assertEqual(self.person_3.name, "Alan Zhang")
        self.assertEqual(self.person_4.name, "Bingshen Yang")

    def test_age(self):
        current_year = datetime.datetime.now().year
        expected_age = current_year - 1990
        self.assertEqual(self.person_1.age, expected_age)
        self.assertEqual(self.person_2.age, expected_age)
        self.assertEqual(self.person_3.age, expected_age)
        self.assertEqual(self.person_4.age, expected_age)

    def test_height(self):
        self.assertEqual(self.person_1.height, 160)
        self.assertEqual(self.person_2.height, 170)
        self.assertEqual(self.person_3.height, 180)
        self.assertEqual(self.person_4.height, 190)

    def test_weight(self):
        self.assertEqual(self.person_1.weight, 90)
        self.assertEqual(self.person_2.weight, 70)
        self.assertEqual(self.person_3.weight, 70)
        self.assertEqual(self.person_4.weight, 80)

    def test_gender(self):
        self.assertEqual(self.person_1.gender, "Male")
        self.assertEqual(self.person_2.gender, "Male")
        self.assertEqual(self.person_3.gender, "Male")
        self.assertEqual(self.person_4.gender, "Male")

    def test_purpose(self):
        self.assertEqual(self.person_1.purpose, "Bulking")
        self.assertEqual(self.person_2.purpose, "Cutting")
        self.assertEqual(self.person_3.purpose, "Cutting")
        self.assertEqual(self.person_4.purpose, "Bulking")

    def test_frequency(self):
        self.assertEqual(self.person_1.frequency, "No exercise")
        self.assertEqual(self.person_2.frequency, "Lightly exercise")
        self.assertEqual(self.person_3.frequency, "Very active")
        self.assertEqual(self.person_4.frequency, "Super active")

if __name__ == '__main__':
    unittest.main()
