import pandas as pd
import matplotlib.pyplot as plt


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
resultNames = []
resultValues = []
    

def calcAvg(dict, keys):
    for x, valx in keys.iteritems():
        dict[keys[x]] = [float(x) for x in dict[keys[x]]]
        numOfThings = len(dict[keys[x]])
        total = sum(dict[keys[x]])
        if numOfThings != 0:
            average = (total/numOfThings)
            average = "{:.2f}".format(average)
        #print(keys[x] +": " +average +"%")
        average = float(average)
        resultNames.append(keys[x])
        resultValues.append(average)


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


#print("Ethnicity Average:")
averageComputing(ethnicity, value)
#print("\n Gender Average:")
averageComputing(gender, value)
#print("\n Free School Meals Average:")
averageComputing(freeSchoolMeals, value)
#print("\n Sen Type Average:")
averageComputing(senType, value)
#print("\n Sen Group Average:")
averageComputing(senGroup, value)
#print("\n Admission Type Average:")
averageComputing(admissionType, value)
#print("\n School Characteristic Average:")
averageComputing(schoolCharacteristic, value)
#print("\n religion Average:")
averageComputing(religion, value)


fig, ax = plt.subplots()

ax.set_title("Bar plot")
ax.bar(resultNames, resultValues)
ax.set_yticks(range(0,100,10))
plt.xticks(rotation=60, ha='right')
plt.show()

