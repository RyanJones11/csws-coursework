import pandas as pd
import matplotlib, csv, pandas as pd
from numpy import average

def totalAverage():
        data = pd.read_csv("data.csv")

        ethnicity = data["Ethnicity"]
        gender = data["Gender"]
        freeSchoolMeals = data["FSM"]
        senType = data["SEN_type"]
        senGroup = data["SEN_grouping"]
        admissionType = data["Admission_type"]
        schoolCharacteristic = data["School_characteristic"]
        religion = data["Religious_denomination"]
        value = data["Value"]
        denominator = data["Denominator"]
        numerator = data["Numerator"]

        def averageComputing(gender):
            variableKeys = [gender.drop_duplicates(keep='first', inplace=False)]
            #for x, valx in variableKeys.iteritems():
              #  for i, val in focus.iteritems():
                 #   if focus[i]==variableKeys[x]:
                  #      print(focus[i])
            print(variableKeys[1])
        averageComputing(gender)
                   
                       