import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#################################################################
#                                                               #
#                                                               #
#                       Load Data                               #
#                                                               #
#                                                               #
#################################################################


# Reads the data from file.
data = pd.read_csv("gcse-english-and-maths-national-data-2019-20.csv")

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
        print("Enter a number between 1-4 or 5 to exit:\n1:Keyword search\n2:Co Efficient\n3:Total Passing\n4:Averages")
        menuSelect=input()
        if menuSelect == "1":
            print("Keyword Search")
            keywordSearch()
            repeat = True
        elif menuSelect == "2":
            print ("Co Efficient")
            CoefficientOfDev(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value)
            repeat =True
        elif menuSelect == "3":
            print ("Total Passing")
            TotalPassing(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value)
            repeat = True
        elif menuSelect == "4":
            print ("Averages")
            averages()
            repeat = True
        elif menuSelect == "5":
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

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")
    
    # Calculates the coefficient of standard deviation for Gender
    def genderCoef(myVariable):
        newList = []
        for i, val in gender.iteritems():
            if gender[i] == myVariable:
                newList.append(value[i])

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

    # Calculates the coefficient of standard deviation for Free School Meals
    def fsmCoef(myVariable):
        newList = []
        for i, val in freeSchoolMeals.iteritems():
            if freeSchoolMeals[i] == myVariable:
                newList.append(value[i])

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

    # Calculates the coefficient of standard deviation for Special Educational Needs Type
    def senTypeCoef(myVariable):
        newList = []
        for i, val in senType.iteritems():
            if senType[i] == myVariable:
                newList.append(value[i])

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

    # Calculates the coefficient of standard deviation for Special Education Needs Group
    def senGroupCoef(myVariable):
        newList = []
        for i, val in senGroup.iteritems():
            if senGroup[i] == myVariable:
                newList.append(value[i])

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

    # Calculates the coefficient of standard deviation for Admission type
    def admisCoef(myVariable):
        newList = []
        for i, val in admissionType.iteritems():
            if admissionType[i] == myVariable:
                newList.append(value[i])

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

    # Calculates the coefficient of standard deviation for School Characteristic
    def schoolCoef(myVariable):
        newList = []
        for i, val in schoolCharacteristic.iteritems():
            if schoolCharacteristic[i] == myVariable:
                newList.append(value[i])

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")

    # Calculates the coefficient of standard deviation for Religion
    def religionCoef(myVariable):
        newList = []
        for i, val in religion.iteritems():
            if religion[i] == myVariable:
                newList.append(value[i])

        print(myVariable, end=":\t\t")
        newList2 = pd.Series(newList)
        print("{:.2f}".format((myCoef(newList2)*100)), end="%\n")


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

    fig, axs = plt.subplots()
    
    axs.bar(CoefVariableList, CoefValueList)

    axs.set_yticks(range(0,100,10))

    axs.set_title("GCSE Results 2019-20", fontsize=14)
    axs.set_xlabel("Group types", fontsize=12)
    axs.set_ylabel("GCSE passing percentage(%)", fontsize=12)

    plt.xticks(rotation = 40, horizontalAlignment = "right")#function for rotating the group names for a better design
    axs.yaxis.grid()

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
        print(focus[i], end=": ")
        print(value[i], end="%\n")

    def CalcPassing(focus, myIndex):
        # Gets total percentage of passing student and percentage of passing students based on ethnicity
        variableKeys = focus.drop_duplicates(keep='first', inplace=False)
        for x, valx in variableKeys.iteritems():
            for i, val in ethnicity.iteritems():
                if myIndex == 1:
                    if ethnicity[i] == variableKeys[x] and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] > -1:
                        PrintPassing(ethnicity, i)
                if myIndex == 2:
                    if ethnicity[i] == "All" and gender[i] == variableKeys[x] and gender[i] != "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] > -1:
                        PrintPassing(gender, i)
                if myIndex == 3:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == variableKeys[x] and freeSchoolMeals[i] != "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] > -1:
                        PrintPassing(freeSchoolMeals, i)
                if myIndex == 4:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == variableKeys[x] and senType[i] != "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] > -1:
                        PrintPassing(senType, i)
                if myIndex == 5:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == variableKeys[x] and senGroup[i] != "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] > -1:
                        PrintPassing(senGroup, i)
                if myIndex == 6:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == variableKeys[x] and admissionType[i] != "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All" and value[i] > -1:
                        PrintPassing(admissionType, i)
                if myIndex == 7:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == variableKeys[x] and schoolCharacteristic[i] != "All state-funded" and religion[i] == "All" and value[i] > -1:
                        PrintPassing(schoolCharacteristic, i)
                if myIndex == 8:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == variableKeys[x] and religion[i] != "All" and value[i] > -1:
                        PrintPassing(religion, i)


    # Changes all 
    for x, valx in value.iteritems():
        if value[x] == "!":
            value[x] = "-1"

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

    

    
#################################################################
#                                                               #
#                                                               #
#                       Key Word Search                         #
#                                                               #
#                                                               #
#################################################################
def keywordSearch():
    data = []
    searchResults = []

    with open("gcse-english-and-maths-national-data-2019-20.csv") as csvfile:#'dataset.csv' to be replaced with the final filename of the dataset
        reader = csv.reader(csvfile)
        for row in reader:#Reads each row of the CSV file
            data.append(row)

    searchTerm = input("Please enter a search term:\n")#Takes the users input to be used as a keyword to search

    for i in range(0,(len(row) - 4)):#Used to only search the columns that contain searchable data.
        column = [x[i] for x in data]
        if searchTerm in column:
            for x in range(0,len(data)):
                if searchTerm == data[x][i]:#This compares the input to the individual value of each "cell" in the CSV file in the data List
                    searchResults.append(data[x])
                    print(searchResults)#Outputs the collected rows that contain the search term.

    if len(searchResults) == 0:
        print("Error:\nNo results match \"" + searchTerm +"\"") #If the searchResults list is empty then an error message is outputted



#################################################################
#                                                               #
#                                                               #
#                           Averages                            #
#                                                               #
#                                                               #
#################################################################
def averages():
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
            print(keys[x] +": " +average +"%")
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

# Runs the menu
menu(ethnicity, gender, freeSchoolMeals, senType, senGroup, admissionType, schoolCharacteristic, religion, value)
