# Training Management Software

## Overview
This software is designed to help users track and manage their health and fitness goals. It consists of several Python modules that work together to provide insights into exercise routines, dietary habits, and overall wellness.

## Main Function
### `start.py`
This module acts as the entry point for the application. It imports necessary modules and initiates the user interface for interaction.

## Subpackage 1 - Person
### `Person.py`
Defines the `Person` class, which encapsulates personal data like name, birthdate, height, weight, gender, purpose, and exercise frequency. This class is central to the application, as it holds user-specific data.

###  Module 1: `calculate.py`
Contains functions to calculate various health metrics, like the Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE), Calories, and other nutrition indicators, using personal data such as gender, weight, height, and age.

### Module 2: `record.py`
Manages user's nutrition records. `record.py` extends the pandas DataFrame for nutrition tracking and allows the user to manage the nutrition record by adding, deleting, modifying and displaying.

## Subpackage 2 - Exercise
### Module 1: `Exercise.py`
This module defines the `Exercise` class, which likely provides recommendations for exercises based on intensity level and targeted body parts.

### Module 2: `Record.py`
This module provides functions like "add", "remove", "modify" and "display", allowing the user to manage the exercise record.

## Usage
To use this application, run the `start.py` script. The user will be prompted to enter their personal details and health goals, which will then be used by the application to provide customized health and fitness recommendations.

## Dependencies
- Python 3
- Pandas: For data manipulation and analysis.
- Pygal (in `record.py`): For generating graphical representations of data.
- IPython (in `record.py` and `Record.py`): For displaying outputs within Jupyter Notebooks.

## Note
Please ensure that all dependencies are installed before running the application.

## Credit to
Xing (Will) Xu
Bingshen (Gevin) Yang
