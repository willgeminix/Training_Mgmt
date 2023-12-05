## Training Management Software Test

#### By Xing (Wil) XU and Bingshen (Gevin) Yang


To use the software, the user needs to import the package first
`from Training_Mgmt import start`

To start the software, run the following code
`start.start()`

The user needs to input the user name. If the username does not exist, the user need to create the user first. 
Sample output:
>Please enter the user name:
>
>The user does NOT exist
>
>Do you want to create the user?
[1]: YES
[q] to quit
[any] for NO:

Input 1 to create the user
>Please create your user.
>
>Please enter the user name:Will
>
>Please enter the birthdate of the newly added record (YYYY-MM-DD):2000-01-01
>
>Please enter the height (cm):100
>
>Please enter the weight (kg):50
>
>Please enter the gender['F'/'M']:M
>
>Please enter the purpose for training
>
>[1] for bulking
>
>[2] for cutting
>
>Choice:2
>
>Please choose the frequecy of exercise.
>
>[1]: No exercise
>
>[2]: 1-2 times per week
>
>[3]: 3-4 times per week
>
>[4]: 5-6 times per week
>
>[5]: more than 6 times per week
>
>Please choose:3

Now the user has been created, the user can use the software by making the choice
> [1]: Calculate Nutrition
>
> [2]: Manipulate the Nutrition Record
>
> [3]: Exercise Suggestion
>
> [4]: Manipulate Exercise Record
>
> [5]: Change Person information
[6]: Exit

When choosing 1, the software will calculate the nutrition indicators based on personal information
>The nutrition indicators based on your personal information are:
>
>BMR (Basal Metabolic Rate):1625.43 kcal/day
>
>TDEE (Total Daily Energy Expenditure): 2519.42kcal/day
>
>Calorie: 1648.42cal
>
>Protein: 292.08g
>
>Carbon: 72.1g
>
>Fat: 37.85g

When choosing 2, the user can manage the nutrition record by adding, deleting, modifying and displaying.

[1]: Add new record

> Please enter the date of the newly added record: `2023-12-01`
>
> Please enter the protein (in g): `100`
>
> Please enter the carbon (in g): `100`
>
> Please enter the fat (in g): `100`

[2]: Delete existed record
>Please enter the date of the record to delete: `2023-12-01`
>
>Are you sure you want to delete the following record?

\\  |Date | Calorie | Protein | Carbon  |  Fat
:---|:---|:---|:---|:---|:---
0 | 2023-12-01 |  1700.0|    100.0|   100.0|  100.0

>Enter 
>
>[1] for "YES"
>
>[2] for "NO and quit"
>
>`Choice:`

[3]: Modify the existed record
>Please enter the date of the record to modify: `2023-12-01`
>
>Which indicators do you want to change?(Calories will be calculated automatically)
[1]: Protein
[2]: Carbon
[3]: Fat
For more than one indicators, seperate the number with ','

`Choice:1,2,3`

Please enter the protein (in g): `200` 

Please enter the carbon (in g): `200`

Please enter the fat (in g): `200`

The record you are going to change:



 \ | Date | Calorie|  Protein|  Carbon|    Fat
:---|:---|:---|:---|:---|:---
 0 | 2023-12-01 |  1700.0 |   100.0 |  100.0 | 100.0
>[1] for YES
[2] for NO and return to the previous menu
`Choice:`

[4]: Display the record

Please enter the start date: `2023-12-01`

Please enter the end date: `2023-12-01`

![test](https://drive.google.com/file/d/1waSSH-GWEbaRhRUsF6f-ffFkRah3rVf8/view?usp=drive_link)

[5]: Return to the previous menu



When choosing 3, the software will give you some exercise suggestions for today, based on your intensity-level

> What do you want to do:
> [1]: Calculate Nutrition
> [2]: Manipulate the Nutrition Record
> [3]: Exercise Suggestion
> [4]: Manipulate Exercise Record
> [5]: Change Person information
> [6]: Exit
> Choice:3
> Please choose the intensity level:
> [1]: easy
> [2]: medium
> [3]: hard
> Choice: 1
> What kind of sports suggestion do you want to ask:
> [1]: Strength
> [2]: Cardio
> [3]: Hybrid
> Choice: 1
> Please choose the body part(s):
> [1]: Chest
> [2]: Shoulder
> [3]: Back
> [4]: Legs
> [5]: Triceps
> [6]: Biceps
> If you want to train multiple body parts, use ',' to separate, e.g. 1,2,3
> However, note that you can't choose more than 3 parts at once, it would be an inappropriate training way
> Choice: 1,2
> Here are the strength exercises recommended for you Today!!! Enjoy your workout!
> Exercise 1: BENCH PRESS [5*5], Youtube Tutorial Link: https://www.youtube.com/watch?v=4Y2ZdHCOXok&pp=ygULYmVuY2ggcHJlc3M%3D
> Exercise 2: INCLINE BENCH PRESS [5*5], Youtube Tutorial Link: https://www.youtube.com/watch?v=SrqOu55lrYU&pp=ygUTaW5jbGluZSBiZW5jaCBwcmVzcw%3D%3D
> Exercise 3: CABLE CROSSOVER [5*12], Youtube Tutorial Link: https://www.youtube.com/watch?v=taI4XduLpTk&pp=ygUPY2FibGUgY3Jvc3NvdmVy
> Exercise 4: DUMBELL INCLINE BENCH PRESS [4*10], Youtube Tutorial Link: https://www.youtube.com/watch?v=8iPEnn-ltC8&pp=ygUbZHVtYmVsbCBpbmNsaW5lIGJlbmNoIHByZXNz
> Exercise 5: DIP PUSH UP [4*12], Youtube Tutorial Link: https://www.youtube.com/watch?v=ybjGSN9IwaA&pp=ygULZGlwIHB1c2ggdXA%3D



When choosing 4, the software will add, remove, modify, display your daily exercise record

> What do you want to do:
> [1]: Calculate Nutrition
> [2]: Manipulate the Nutrition Record
> [3]: Exercise Suggestion
> [4]: Manipulate Exercise Record
> [5]: Change Person information
> [6]: Exit
> Choice:4
> What do you want to do with your exercise record:
> [1]: Add new record
> [2]: Delete existed record
> [3]: Modify the existed record
> [4]: Display the record
> [5]: Return to the previous menu
> Choice:1
> Please enter the date of the exercise: 2023-12-01
> Please enter the name of the exercise: bench pres
> Please enter the number of the sets: 5
> Please enter the number of the reps: 5
> What do you want to do with your exercise record:
> [1]: Add new record
> [2]: Delete existed record
> [3]: Modify the existed record
> [4]: Display the record
> [5]: Return to the previous menu
> Choice:3
> Please enter the index you want to modify: 0
> Please enter the new date: 2023-12-02
> Please enter the new exercise name: bench press
> Please enter the new exercise sets: 5
> Please enter the new exercise reps: 10
> What do you want to do with your exercise record:
> [1]: Add new record
> [2]: Delete existed record
> [3]: Modify the existed record
> [4]: Display the record
> [5]: Return to the previous menu
> Choice:4
>  ID       date exercise_name  exercise_set  exercise_rep
>   0 2023-12-02   bench press             5            10

When choosing 5, the software will calculate the nutrition indicators based on personal information

> What do you want to do:
> [1]: Calculate Nutrition
> [2]: Manipulate the Nutrition Record
> [3]: Exercise Suggestion
> [4]: Manipulate Exercise Record
> [5]: Change Person information
> [6]: Exit
> Choice:5
> Which person information do you want to change?
> [1]: Height
> [2]: Weight
> [3]: Purpose
> [4]: Frequency
> [5]: Return to the previous menu.
> Choice:1
> Please enter your new height (cm):177