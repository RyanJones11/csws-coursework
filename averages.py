import matplotlib, csv, pandas as pd
from numpy import average

data = pd.read_csv("data.csv")

gender = data["Gender"]
value = data["Value"]


sum = 0  
sum2 = 0      
boys = []
for i, val in gender.iteritems():
    if gender[i] == "Boys":
        sum2 = sum2+1
        if value[i] == '!':
            value[i] = 0
        f = float(value[i])
        boys.append(f)
        sum = sum + f
print(boys)
print(sum)
print(sum2)
average = sum/sum2
average = "{:.2f}".format(average)
print(average)