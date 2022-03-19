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


print(type(value[0]))

def calcAvg(dict):
  dict["Boys"] = [float(x) for x in dict["Boys"]]
  print(len(dict["Boys"]))
  numOfTings = len(dict["Boys"])
  total = sum(dict["Boys"])
  print(type(dict["Boys"][0]))
  print(dict["Boys"][0])
  print(total)
  print(numOfTings)
  average = (total/numOfTings)
  average = "{:.2f}".format(average)
  print(average)
  

def averageComputing(criteria, value):
  keys = criteria.drop_duplicates(keep = "first", inplace = False)
  dict = {}
  for n in keys:
    dict[n] = []

  for x, valx in keys.iteritems():
    for i, val in criteria.iteritems():
      if keys[x] == criteria[i]:
        if value[i] != "!":
          dict[gender[i]].append(value[i])
  calcAvg(dict)
  

        
        

averageComputing(gender, value)
