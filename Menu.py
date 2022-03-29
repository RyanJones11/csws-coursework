from Coursework import TotalPassing


def menu():
    repeat=True
    while repeat==True:
        menuSelect=0
        print("Enter a number between 1-4: ")
        menuSelect=input()
        if menuSelect == "1":
            print("Keyword Search")
            repeat = True
        elif menuSelect == "2":
            print ("Co efficient")
            CoefficientOfDev()
            repeat =True
        elif menuSelect == "3":
            print ("Total Passing")
            TotalPassing()
            repeat = True
        elif menuSelect == "4":
            print ("Averages")
            repeat = True
        else:
            print ("Invalid answer, please reenter")
            repeat = True
menu()