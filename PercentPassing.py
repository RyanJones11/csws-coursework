import pandas as pd

def TotalPassing():
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

    # Gets total percentage of passing student and percentage of passing students based on ethnicity
    variableKeys = ethnicity.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in ethnicity.iteritems():
            if ethnicity[i] == variableKeys[x] and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                print(ethnicity[i], end=": ")
                print(value[i], end="%\n")

    # Gender
    variableKeys = gender.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in gender.iteritems():
            if ethnicity[i] == "All" and gender[i] == variableKeys[x] and gender[i] != "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                print(gender[i], end=": ")
                print(value[i], end="%\n")

    # Free School Meals
    variableKeys = freeSchoolMeals.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in freeSchoolMeals.iteritems():
            if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == variableKeys[x] and freeSchoolMeals[i] != "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                print(freeSchoolMeals[i], end=": ")
                print(value[i], end="%\n")

    # SEN Type
    variableKeys = senType.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in senType.iteritems():
            if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == variableKeys[x] and senType[i] != "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                print(senType[i], end=": ")
                print(value[i], end="%\n")

    # SEN Group
    variableKeys = senGroup.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in senGroup.iteritems():
            if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == variableKeys[x] and senGroup[i] != "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                print(senGroup[i], end=": ")
                print(value[i], end="%\n")

    # Admission Type
    variableKeys = admissionType.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in admissionType.iteritems():
            if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == variableKeys[x] and admissionType[i] != "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == "All":
                print(admissionType[i], end=": ")
                print(value[i], end="%\n")

    # School Characteristics
    variableKeys = schoolCharacteristic.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in schoolCharacteristic.iteritems():
            if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == variableKeys[x] and schoolCharacteristic[i] != "All state-funded" and religion[i] == "All":
                print(schoolCharacteristic[i], end=": ")
                print(value[i], end="%\n")

    # Religion
    variableKeys = religion.drop_duplicates(keep='first', inplace=False)
    for x, valx in variableKeys.iteritems():
        for i, val in schoolCharacteristic.iteritems():
            if ethnicity[i] == "All" and gender[i] == "All" and freeSchoolMeals[i] == "All" and senType[i] == "All" and senGroup[i] == "All" and admissionType[i] == "All" and schoolCharacteristic[i] == "All state-funded" and religion[i] == variableKeys[x] and religion[i] != "All":
                print(religion[i], end=": ")
                print(value[i], end="%\n")

TotalPassing()
