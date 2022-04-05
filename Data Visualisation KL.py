from turtle import color, width
import pandas as pd
import matplotlib.pyplot as plt
import numpy

## creates series
variableList = []
variableValues = []

data = pd.read_csv("dataset.csv", na_values=["!"])
data.dropna() #function too drop all null values

ethnicity_values = data ["Ethnicity"]
sen_values = data["SEN_type"]
fsm_values = data["FSM"]
gender_values = data["Gender"]
admission_values = data["Admission_type"]
schoolChar_values = data["School_characteristic"]
religion_values = data["Religious_denomination"]
Score_values = data["Value"]

fig, axs = plt.subplots()

axs.set_yticks(range(0,100,10))

axs.set_title("GCSE Results 2019-20", fontsize=14)
axs.set_xlabel("Group types", fontsize=12)
axs.set_ylabel("GCSE passing percentage(%)", fontsize=12)

axs.bar(ethnicity_values, Score_values, width=0.5, color= "black")
axs.bar(gender_values, Score_values, width= 0.5, color= "yellow")
axs.bar(religion_values, Score_values, width= 0.5, color= "blue")
axs.bar(sen_values, Score_values, width= 0.5, color ="red")
axs.bar(fsm_values, Score_values, width= 0.5, color ="orange")
axs.bar(schoolChar_values, Score_values, width= 0.5, color="green")
axs.bar(admission_values, Score_values, width=0.5, color="brown")#function for displaying data with width and color values

plt.xticks(rotation = 40, horizontalAlignment = "right")#function for rotating the group names for a better design
axs.yaxis.grid()

plt.tight_layout()
plt.show()
