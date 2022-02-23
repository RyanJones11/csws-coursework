import pandas as pd
import math


# Calculates coeficient of variation.
def myCoef(myInput):
    mean = 0
    total = 0
    counter = 0

    for i, val in myInput.iteritems():
        mean = mean + myInput[i]
        counter = counter + 1

    mean = mean/counter
    count = 0

    myInput2 = []
    for i, val in myInput.iteritems():
        myInput2.append((myInput[i]-mean) ** 2)

    for i, val in myInput.iteritems():
        total = myInput2[i] + total
        count = count + 1


    next = total/count
    next = math.sqrt(total/count)

    next = next/mean
    return next

def ethnicityCoef(myVariable):
    newList = []
    for i, val in ethnicity.iteritems():
        if ethnicity[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

def genderCoef(myVariable):
    newList = []
    for i, val in gender.iteritems():
        if gender[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

def fsmCoef(myVariable):
    newList = []
    for i, val in freeSchoolMeals.iteritems():
        if freeSchoolMeals[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

def senTypeCoef(myVariable):
    newList = []
    for i, val in senType.iteritems():
        if senType[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

def senGroupCoef(myVariable):
    newList = []
    for i, val in senGroup.iteritems():
        if senGroup[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

def admisCoef(myVariable):
    newList = []
    for i, val in admissionType.iteritems():
        if admissionType[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

def schoolCoef(myVariable):
    newList = []
    for i, val in schoolCharacteristic.iteritems():
        if schoolCharacteristic[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

def religionCoef(myVariable):
    newList = []
    for i, val in religion.iteritems():
        if religion[i] == myVariable:
            newList.append(value[i])

    print(myVariable, end=":\t\t")
    newList2 = pd.Series(newList)
    print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

# Reads the data from file.
data = pd.read_csv("data.csv")

# Load required columns
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

myKeys = ethnicity.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    ethnicityCoef(myKeys[i])


######
myKeys = []
myKeys = gender.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    genderCoef(myKeys[i])

######
myKeys = []
myKeys = freeSchoolMeals.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    fsmCoef(myKeys[i])

######
myKeys = []
myKeys = senType.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    senTypeCoef(myKeys[i])

######
myKeys = []
myKeys = senGroup.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    senGroupCoef(myKeys[i])

######
myKeys = []
myKeys = admissionType.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    admisCoef(myKeys[i])

######
myKeys = []
myKeys = schoolCharacteristic.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    schoolCoef(myKeys[i])

######
myKeys = []
myKeys = religion.drop_duplicates(keep='first', inplace=False)

for i, val in myKeys.iteritems():
    religionCoef(myKeys[i])

