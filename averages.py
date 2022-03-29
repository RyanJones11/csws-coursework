import pandas as pd
import matplotlib.pyplot as plt
#imprting required libaries

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
 #creating lists from the coloumn in the data set and to store the results   

def calcAvg(dict, keys):
    #function to calculate an average from the list for each coloumn used from the dataset 
    #and then to append those values to a list to store the results
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
    #function get required search words, turn them into individual lists and then to populate 
    #arrays with the required data and then to pass the dictionary of lists and key words into the calculating 
    #average function
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

#passing the required parameters into the first function to allow the data to be processed
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
