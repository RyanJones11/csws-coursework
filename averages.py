import matplotlib, csv, pandas as pd
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

def gender_avg():
    bSum = 0  
    gSum = 0
    aSum = 0
    bSum2 = 0  
    gSum2 = 0
    aSum2 = 0
    
    for i, val in gender.iteritems():
        if gender[i] == "Boys":
            if value[i] == '!':
                value[i] = 0
            f = float(value[i])
        if value[i] =="Boys":
            bSum2 = bSum2+1
            bsum = bsum + f
        if value[i] =="Girls":
            gSum2 = gSum2+1
            gSum = gSum + f
        if value[i] =="All":
            aSum2 = aSum2+1
            asum = asum + f
    print(bSum2)
    
    gender_avg()