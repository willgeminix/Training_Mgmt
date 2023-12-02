import os
import pandas as pd
import re


def get_date(prompt):
    while True:
        new_date = input(prompt)
        re_bdate = r'\d{4}/\d{2}/\d{2}'
        if not re.match(re_bdate, new_date):
            print("The date does not follow the required format, please check and try again.")
            continue
        elif new_date[5:7] not in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            print("The MONTH does NOT align with the format, please check and enter again.")
            continue
        elif (not new_date[8:].isnumeric()) or (int(new_date[8:])<=0) or (int(new_date[8:])>31):
            print("The DAY does NOT align with the format, please check and enter again.")
            continue
        else:
            return new_date
        
#date = get_date("lll:")
date = '2023-12-01'
df = pd.read_csv(os.getcwd()+"\\1_nutrition.csv")
print(df["Date"], type(df["Date"][0]))
print(df[df["Date"]==date])