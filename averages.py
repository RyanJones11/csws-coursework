import pandas as pd
import matplotlib
import csv
import pandas as pd
from numpy import average


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


def calcAvg(dict, keys):
  average = 0
  for x, valx in keys.iteritems():
    dict[keys[x]] = [float(x) for x in dict[keys[x]]]
    numOfThings = len(dict[keys[x]])
    total = sum(dict[keys[x]])
    if numOfThings != 0:
      average = (total/numOfThings)
      average = "{:.2f}".format(average)
    print(keys[x] +": " +average +"%")

def averageComputing(criteria, value):
    keys = criteria.drop_duplicates(keep="first", inplace=False)
    dict = {}
    for n in keys:
        dict[n] = []

    for x, valx in keys.iteritems():
        for i, val in criteria.iteritems():
            if keys[x] == criteria[i]:
                if value[i] != "!":
                    dict[criteria[i]].append(value[i])
    calcAvg(dict, keys)

averageComputing(ethnicity, value)
averageComputing(gender, value)
averageComputing(freeSchoolMeals, value)
averageComputing(senType, value)
averageComputing(senGroup, value)
averageComputing(admissionType, value)
averageComputing(schoolCharacteristic, value)
averageComputing(religion, value)

