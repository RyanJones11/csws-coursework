from numpy import append
import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# This program creates visualisations based off data processed through
# differnt algorithms.
# 1: Calculates the amount of variance/coeficcient per group.
# 2: Total percentage of students from each category that achieved grade 5-9.
# 3: The average pass percentage of a record containing.
# 4: Exits the application.

#################################################################
#                                                               #
#                                                               #
#                       Load Data                               #
#                                                               #
#                                                               #
#################################################################


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




#################################################################
#                                                               #
#                                                               #
#                       Menu Function                           #
#                                                               #
#                                                               #
#################################################################
def menu(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value):
    repeat=True
    while repeat==True:
        menuSelect=0
        print("Enter a number between 1-4 or 5 to exit:\n1:Co Efficient\n2:Total Passing\n3:Averages\n4:Exit")
        menuSelect=input()
        if menuSelect == "1":
            print ("Co Efficient")
            CoefficientOfDev(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value)
            repeat =True
        elif menuSelect == "2":
            print ("Total Passing")
            TotalPassing(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value)
            repeat = True
        elif menuSelect == "3":
            print ("Averages")
            averages(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value)
            repeat = True
        elif menuSelect == "4":
            print("menu exit")
            repeat = False
        else:
            print ("Invalid answer, please re enter")
            repeat = True
#################################################################
#                                                               #
#                                                               #
#         Calculate Coefficient of Standard Deviation           #
#                                                               #
#                                                               #
#################################################################
def CoefficientOfDev(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value):
    # Calculates coeficient of variation.


    # Creates Series
    CoefVariableList = []
    CoefValueList = []

    # Calculated Coefficient
    def myCoef(myInput):
        mean = 0
        total = 0
        counter = 0

    
        # Calculates total of all the values of myInput
        for i, val in myInput.iteritems():
            if myInput[i] != -1:
                mean = mean + myInput[i]
                counter = counter + 1

        # Calculates mean
        mean = mean/counter

        # Initiates count to 0
        count = 0

        # Appends to myInput2
        myInput2 = []
        for i, val in myInput.iteritems():
            myInput2.append((myInput[i]-mean) ** 2)

        # Adds up total and increases count
        for i, val in myInput.iteritems():
            total = myInput2[i] + total
            count = count + 1

        # Calculates mean
        next = total/count

        #Calculates square root of mean
        next = math.sqrt(total/count)

        # Divides by mean
        next = next/mean

        # Returns the coefficient of standard deviation
        return next

    # Calculates the coefficient of standard deviation for Ethnicity
    def ethnicityCoef(myVariable):
        newList = []
        for i, val in ethnicity.iteritems():
            if ethnicity[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)
    
    # Calculates the coefficient of standard deviation for Gender
    def genderCoef(myVariable):
        newList = []
        for i, val in gender.iteritems():
            if gender[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)

    # Calculates the coefficient of standard deviation for Free School Meals
    def fsmCoef(myVariable):
        newList = []
        for i, val in freeSchoolMeals.iteritems():
            if freeSchoolMeals[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)

    # Calculates the coefficient of standard deviation for Special Educational Needs Type
    def senTypeCoef(myVariable):
        newList = []
        for i, val in senType.iteritems():
            if senType[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)

    # Calculates the coefficient of standard deviation for Special Education Needs Group
    def senGroupCoef(myVariable):
        newList = []
        for i, val in senGroup.iteritems():
            if senGroup[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)

    # Calculates the coefficient of standard deviation for Admission type
    def admisCoef(myVariable):
        newList = []
        for i, val in admissionType.iteritems():
            if admissionType[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)

    # Calculates the coefficient of standard deviation for School Characteristic
    def schoolCoef(myVariable):
        newList = []
        for i, val in schoolCharacteristic.iteritems():
            if schoolCharacteristic[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)

    # Calculates the coefficient of standard deviation for Religion
    def religionCoef(myVariable):
        newList = []
        for i, val in religion.iteritems():
            if religion[i] == myVariable:
                newList.append(value[i])

        CoefVariableList.append(myVariable)
        newList2 = pd.Series(newList)
        CoefValueList.append(myCoef(newList2)*100)


    # Drops duplicates to make list of key terms
    myKeys = ethnicity.drop_duplicates(keep='first', inplace=False)

    # Filters out "All" term from key terms
    myKeys = myKeys[myKeys!='All']

    # Replaces all "!" which signifies null value with negative so all series can be numerical but still avoided
    for i, val in value.iteritems():
        if value[i] == '!':
            value[i] = -1

    # Converts series to numerical
    value = pd.to_numeric(value)

    # Caluates Coefficient of Standard Deviation for each term in key terms (Ethnicity)
    for i, val in myKeys.iteritems():
        ethnicityCoef(myKeys[i])

    # Caluates Coefficient of Standard Deviation for each term in key terms (Gender)
    myKeys = []
    myKeys = gender.drop_duplicates(keep='first', inplace=False)
    myKeys = myKeys[myKeys!='All']

    for i, val in myKeys.iteritems():
        genderCoef(myKeys[i])

    # Caluates Coefficient of Standard Deviation for each term in key terms (Free School Meals)
    myKeys = []
    myKeys = freeSchoolMeals.drop_duplicates(keep='first', inplace=False)
    myKeys = myKeys[myKeys!='All']

    for i, val in myKeys.iteritems():
        fsmCoef(myKeys[i])

    # Caluates Coefficient of Standard Deviation for each term in key terms (Special Educational Needs Type)
    myKeys = []
    myKeys = senType.drop_duplicates(keep='first', inplace=False)
    myKeys = myKeys[myKeys!='All']

    for i, val in myKeys.iteritems():
        senTypeCoef(myKeys[i])

    # Caluates Coefficient of Standard Deviation for each term in key terms (Special Educational Needs Group)
    myKeys = []
    myKeys = senGroup.drop_duplicates(keep='first', inplace=False)
    myKeys = myKeys[myKeys!='All']

    for i, val in myKeys.iteritems():
        senGroupCoef(myKeys[i])

    # Caluates Coefficient of Standard Deviation for each term in key terms (Admission Type)
    myKeys = []
    myKeys = admissionType.drop_duplicates(keep='first', inplace=False)
    myKeys = myKeys[myKeys!='All']

    for i, val in myKeys.iteritems():
        admisCoef(myKeys[i])

    # Caluates Coefficient of Standard Deviation for each term in key terms (School Characteristic)
    myKeys = []
    myKeys = schoolCharacteristic.drop_duplicates(keep='first', inplace=False)
    myKeys = myKeys[myKeys!='All state-funded']
    myKeys = myKeys[myKeys!='All']

    for i, val in myKeys.iteritems():
        schoolCoef(myKeys[i])

    # Caluates Coefficient of Standard Deviation for each term in key terms (Religion)
    myKeys = []
    myKeys = religion.drop_duplicates(keep='first', inplace=False)
    myKeys = myKeys[myKeys!='Hindu']
    myKeys = myKeys[myKeys!='All']

    for i, val in myKeys.iteritems():
        religionCoef(myKeys[i])

    fig, ax = plt.subplots()

    plt.title("Scatter Graph\n To Show the Amount of Variation Per Group")
    ax.set_xlabel("Variable", fontsize=12)
    ax.set_ylabel("Percentage", fontsize=12)
    ax.scatter(CoefVariableList, CoefValueList)
    ax.set_yticks(range(0,200,20))
    plt.xticks(rotation=60, ha='right')
    plt.tight_layout()
    plt.show()
    

#################################################################
#                                                               #
#                                                               #
#                 Passing Percentage per Group                  #
#                                                               #
#                                                               #
#################################################################
def TotalPassing(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value):

    # Creates Lists
    variableList = []
    valueList = []


    # Appends variable and associated value to list to be displayed.
    def PrintPassing(focus, i):
        variableList.append(focus[i])
        valueList.append(value[i])

    def CalcPassing(focus, myIndex):
        # Gets total percentage of passing student and percentage of passing students based on ethnicity
        variableKeys = focus.drop_duplicates(keep='first', inplace=False)
        for x, valx in variableKeys.iteritems():
            for i, val in ethnicity.iteritems():
                if myIndex == 1:
                    if ethnicity[i] == variableKeys[x] and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] < 101:
                        PrintPassing(ethnicity, i)
                if myIndex == 2:
                    if ethnicity[i] == "All" and gender[i] == variableKeys[x] and gender[i] != "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] < 101:
                        PrintPassing(gender, i)
                if myIndex == 3:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == variableKeys[x] and freeSchoolMeals[i] != "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] < 101:
                        PrintPassing(freeSchoolMeals, i)
                if myIndex == 4:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == variableKeys[x] and senType[i] != "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] < 101:
                        PrintPassing(senType, i)
                if myIndex == 5:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == variableKeys[x] and senGroup[i] != "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] < 101:
                        PrintPassing(senGroup, i)
                if myIndex == 6:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == variableKeys[x] and admissionType[i] != "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] < 101:
                        PrintPassing(admissionType, i)
                if myIndex == 7:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == variableKeys[x] and schoolCharacteristic[i] != "All state-funded" and religion[i] == "All" and value[i] < 101:
                        PrintPassing(schoolCharacteristic, i)
                if myIndex == 8:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == variableKeys[x] and religion[i] != "All" and value[i] < 101:
                        PrintPassing(religion, i)


    # Changes all 
    for x, valx in value.iteritems():
        if value[x] == "!":
            value[x] = "200"

    # Changes all values to numeric
    value = pd.to_numeric(value)

    # Calculate passing grade for each column
    CalcPassing(ethnicity, 1)
    CalcPassing(gender, 2)
    CalcPassing(freeSchoolMeals, 3)
    CalcPassing(senType, 4)
    CalcPassing(senGroup, 5)
    CalcPassing(admissionType, 6)
    CalcPassing(schoolCharacteristic, 7)
    CalcPassing(religion, 8)

    fig, ax = plt.subplots()

    plt.title("Bar Chart\n To show average percentage of students achieveing grades 5-9")
    ax.set_xlabel("Variable", fontsize=12)
    ax.set_ylabel("Percentage", fontsize=12)
    ax.bar(variableList, valueList)
    ax.set_yticks(range(0,100,10))
    plt.xticks(rotation=60, ha='right')
    plt.tight_layout()
    plt.show()



#################################################################
#                                                               #
#                                                               #
#                           Averages                            #
#                                                               #
#                                                               #
#################################################################
def averages(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value):
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
    averageComputing(ethnicity, value)
    
    averageComputing(gender, value)
    
    averageComputing(freeSchoolMeals, value)
    
    averageComputing(senType, value)
    
    averageComputing(senGroup, value)

    averageComputing(admissionType, value)

    averageComputing(schoolCharacteristic, value)

    averageComputing(religion, value)

    fig, ax = plt.subplots()

    plt.title("Scatter Graph \n To show average percentage of students achieveing grades 5-9")
    ax.set_xlabel("Variable", fontsize=12)
    ax.set_ylabel("Percentage", fontsize=12)
    ax.scatter(resultNames, resultValues)
    #ax.plot(resultNames,averageList)
    ax.set_yticks(range(0,100,10))
    plt.xticks(rotation=60, ha='right')
    plt.tight_layout()
    plt.show()

    print("Done")





# Runs the menu
menu(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value)
