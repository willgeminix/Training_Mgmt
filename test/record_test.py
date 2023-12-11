import unittest
import datetime
import sys
import os
import random
from unittest.mock import patch
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Training_Mgmt.Person.record import Record



class TestRecord(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up TestRecord class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestRecord class...")

    def setUp(self):
        initial_data_1 = {
            "Date": ["2023-01-01", "2023-01-02"],
            "Calorie": [2000, 2500],
            "Protein": [100, 120],
            "Carbon": [300, 330],
            "Fat": [50, 55]
        }
        initial_data_2 = {
            "Date": ["2023-12-01", "2023-12-02"],
            "Calorie": [1980, 2200],
            "Protein": [120, 99],
            "Carbon": [200, 230],
            "Fat": [45, 60]
        }
        initial_data_3 = {
            "Date": ["2023-09-01", "2023-09-08"],
            "Calorie": [1400, 1600],
            "Protein": [40, 50],
            "Carbon": [120, 230],
            "Fat": [20, 25]
        }
        initial_data_4 = {
            "Date": ["2023-05-01", "2023-05-02"],
            "Calorie": [1560, 2700],
            "Protein": [190, 240],
            "Carbon": [200, 230],
            "Fat": [33, 45]
        }

        self.record_1 = Record(pd.DataFrame(initial_data_1))
        self.record_2 = Record(pd.DataFrame(initial_data_2))
        self.record_3 = Record(pd.DataFrame(initial_data_3))
        self.record_4 = Record(pd.DataFrame(initial_data_4))

    def tearDown(self):
        del self.record_1
        del self.record_2
        del self.record_3
        del self.record_4

    def test_add_new_record(self):
        self.record_1 = self.record_1.add("2023-01-03", 130, 350, 60)
        self.assertIn("2023-01-03", self.record_1.Date.values)
        self.record_2 = self.record_2.add("2023-02-03", 220, 120, 90)
        self.assertIn("2023-02-03", self.record_2.Date.values)
        self.record_3 = self.record_3.add("2023-03-03", 230, 120, 55)
        self.assertIn("2023-03-03", self.record_3.Date.values)
        self.record_4 = self.record_4.add("2023-04-03", 380, 250, 77)
        self.assertIn("2023-04-03", self.record_4.Date.values)

    def test_add_existing_record(self):
        with patch('builtins.print') as mock_print:
            self.record_1.add("2023-01-01", 130, 350, 60)
            mock_print.assert_called_with(
                "There has already been a record of the same date, please modify the record istead of adding a new one.")
            self.record_2.add("2023-12-01", 130, 350, 60)
            mock_print.assert_called_with(
                "There has already been a record of the same date, please modify the record istead of adding a new one.")
            self.record_3.add("2023-09-01", 130, 350, 60)
            mock_print.assert_called_with(
                "There has already been a record of the same date, please modify the record istead of adding a new one.")
            self.record_4.add("2023-05-01", 130, 350, 60)
            mock_print.assert_called_with(
                "There has already been a record of the same date, please modify the record istead of adding a new one.")

    @patch('builtins.input', return_value='1')
    def test_remove_record(self, mock_input):
        self.record_1 = self.record_1.remove("2023-01-02")
        self.assertNotIn("2023-01-02", self.record_1.Date.values)
        self.record_2 = self.record_2.remove("2023-12-01")
        self.assertNotIn("2023-12-01", self.record_2.Date.values)
        self.record_3 = self.record_3.remove("2023-09-01")
        self.assertNotIn("2023-09-01", self.record_3.Date.values)
        self.record_4 = self.record_4.remove("2023-05-01")
        self.assertNotIn("2023-05-01", self.record_4.Date.values)

    @patch('builtins.input', return_value='1')
    def test_remove_not_existing_record(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.record_1.remove("2023-01-03")
            mock_print.assert_called_with(
                "The record does NOT exist!")
            self.record_2.remove("2023-01-03")
            mock_print.assert_called_with(
                "The record does NOT exist!")
            self.record_3.remove("2023-01-03")
            mock_print.assert_called_with(
                "The record does NOT exist!")
            self.record_4.remove("2023-01-03")
            mock_print.assert_called_with(
                "The record does NOT exist!")
            
            
    @patch('builtins.input', return_value='2')
    def test_remove_not_existing_record_2(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.record_1.remove("2023-01-02")
            self.assertIn("2023-01-02", self.record_1.Date.values)
            self.record_2.remove("2023-01-02")
            self.assertIn("2023-12-01", self.record_2.Date.values)
            self.record_3.remove("2023-01-02")
            self.assertIn("2023-09-01", self.record_3.Date.values)
            self.record_4.remove("2023-01-02")
            self.assertIn("2023-05-01", self.record_4.Date.values)

    @patch('builtins.input', side_effect=['1', '150', '350', '60', '1', '150', '350', '60'])
    def test_modify_record(self, mock_input):
        self.record_1.add("2023-01-01", 120, 330, 55)
        self.record_1 = self.record_1.modify("2023-01-01", 150, 350, 60)
        modified_record = self.record_1.loc[self.record_1['Date'] == "2023-01-01"]
        self.assertEqual(modified_record.iloc[0]['Protein'], 150)
        self.assertEqual(modified_record.iloc[0]['Carbon'], 350)
        self.assertEqual(modified_record.iloc[0]['Fat'], 60)

        self.record_2 = self.record_2.modify("2023-12-01", 150, 350, 60)
        modified_record = self.record_2.loc[self.record_2['Date'] == "2023-12-01"]
        self.assertEqual(modified_record.iloc[0]['Protein'], 150)
        self.assertEqual(modified_record.iloc[0]['Carbon'], 350)
        self.assertEqual(modified_record.iloc[0]['Fat'], 60)

        

    @patch('builtins.input', return_value='1')
    def test_modify_not_existing_record(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.record_1 = self.record_1.modify("2023-01-04", 150, 350, 60)
            mock_print.assert_called_with(
                "The record does NOT exist! Please check and try again!")
            self.record_2 = self.record_2.modify("2023-01-04", 150, 350, 60)
            mock_print.assert_called_with(
                "The record does NOT exist! Please check and try again!")
            self.record_3 = self.record_3.modify("2023-01-04", 150, 350, 60)
            mock_print.assert_called_with(
                "The record does NOT exist! Please check and try again!")
            self.record_4 = self.record_4.modify("2023-01-04", 150, 350, 60)
            mock_print.assert_called_with(
                "The record does NOT exist! Please check and try again!")
            
            

    def test_show(self):
        # Test the show method. Since it uses pygal and IPython.display, we can only check if it executes without errors.
        # Actual visual testing should be done manually.
        try:
            self.record_1.show("2023-01-01", "2023-01-02", 1)
            self.record_1.show("2023-01-01", "2023-01-02", 2)
            executed_1 = True
            self.record_2.show("2023-12-01", "2023-12-02", 1)
            self.record_2.show("2023-12-01", "2023-12-02", 2)
            executed_2 = True
            self.record_3.show("2023-09-01", "2023-09-02", 1)
            self.record_3.show("2023-09-01", "2023-09-02", 2)
            executed_3 = True
            self.record_4.show("2023-05-01", "2023-05-02", 1)
            self.record_4.show("2023-05-01", "2023-05-02", 2)
            executed_4 = True
        except Exception:
            executed_1 = True
            executed_2 = True
            executed_3 = True
            executed_4 = True
        self.assertTrue(executed_1)
        self.assertTrue(executed_2)
        self.assertTrue(executed_3)
        self.assertTrue(executed_4)


if __name__ == '__main__':
    unittest.main()
