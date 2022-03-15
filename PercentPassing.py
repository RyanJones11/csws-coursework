import pandas as pd

def TotalPassing():

    def PrintPassing(focus, i):
        print(focus[i], end=": ")
        print(value[i], end="%\n")

    def CalcPassing(focus, myIndex):
        # Gets total percentage of passing student and percentage of passing students based on ethnicity
        variableKeys = focus.drop_duplicates(keep='first', inplace=False)
        for x, valx in variableKeys.iteritems():
            for i, val in ethnicity.iteritems():
                if myIndex == 1:
                    if ethnicity[i] == variableKeys[x] and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                        PrintPassing(ethnicity, i)
                if myIndex == 2:
                    if ethnicity[i] == "All" and gender[i] == variableKeys[x] and gender[i] != "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                        PrintPassing(gender, i)
                if myIndex == 3:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == variableKeys[x] and freeSchoolMeals[i] != "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                        PrintPassing(freeSchoolMeals, i)
                if myIndex == 4:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == variableKeys[x] and senType[i] != "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                        PrintPassing(senType, i)
                if myIndex == 5:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == variableKeys[x] and senGroup[i] != "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                        PrintPassing(senGroup, i)
                if myIndex == 6:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == variableKeys[x] and admissionType[i] != "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                        PrintPassing(admissionType, i)
                if myIndex == 7:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == variableKeys[x] and schoolCharacteristic[i] != "All state-funded" and religion[i] == "All":
                        PrintPassing(schoolCharacteristic, i)
                if myIndex == 8:
                    if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == variableKeys[x] and religion[i] != "All":
                        PrintPassing(religion, i)

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

    CalcPassing(ethnicity, 1)
    CalcPassing(gender, 2)
    CalcPassing(freeSchoolMeals, 3)
    CalcPassing(senType, 4)
    CalcPassing(senGroup, 5)
    CalcPassing(admissionType, 6)
    CalcPassing(schoolCharacteristic, 7)
    CalcPassing(religion, 8)

TotalPassing()
