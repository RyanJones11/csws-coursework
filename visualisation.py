
import pandas as pd                                     #Imports the required libraries that are needed to run the code
from turtle import color, width                         
import matplotlib.pyplot as plt                         

data = pd.read_csv("dataset.csv", na_values = ["!"])    #Allows Pandas to read the file and 
data.dropna()                                           #drops all null values that in the original file is marked with !

fsm = data["FSM"]                                       #Using variables to access the functions in pandas to read the FSM column of the file
percentagePassed = data["Value"]                        #Using variables to access the functions in pandas to read the Value column of the file

fig, ax = plt.subplots()                                #Imports the axis

ax.set_yticks(range(0,110,10))                          #Sets the increments that the Y value increases by each step

ax.set_title("Average Grades between those on FSM and those who are not.", fontsize=14)
ax.set_ylabel("Grade Percentage(%)", fontsize=12)
ax.set_xlabel("Whether Free school meals are available", fontsize=12)

ax.bar(fsm, percentagePassed, width=0.5, color="green") #Plots the bars that represent each of the options in the FSM column 
ax.yaxis.grid()
plt.show()

