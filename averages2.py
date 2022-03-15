import matplotlib, csv, pandas as pd
from numpy import average

data = pd.read_csv("data.csv")

gender = data["Gender"]
value = data["Value"]


bSum = 0  
bSum2 = 0     
gSum = 0  
gSum2 = 0 
aSum = 0  
aSum2 = 0  

for i, val in gender.iteritems():
    if gender[i] == "Boys":
        bSum2 = bSum2+1
        if value[i] == '!':
            value[i] = 0
        f = float(value[i])
        bSum = bSum + f
    if gender[i] == "Girls":
        gSum2 = gSum2+1
        if value[i] == '!':
            value[i] = 0
        f = float(value[i])
        gSum = gSum + f
    if gender[i] == "All":
        aSum2 = aSum2+1
        if value[i] == '!':
            value[i] = 0
        f = float(value[i])
        aSum = aSum + f

bAverage = bSum/bSum2
bAverage = "{:.2f}".format(bAverage)
print("Boys average:" +bAverage)

gAverage = gSum/gSum2
gAverage = "{:.2f}".format(gAverage)
print("Girls average:" +gAverage)

aAverage = aSum/aSum2
aAverage = "{:.2f}".format(aAverage)
print("All average:" +aAverage)