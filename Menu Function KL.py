def menu():
    repeat=True
    while repeat==True:
        menuSelect=0
        print("Enter a number between 1-4 or 5 to exit:")
        menuSelect=input()
        if menuSelect == "1":
            print("Keyword search")
            repeat = True
        elif menuSelect == "2":
            print ("Passing percentage")
            #TotalPassing()
            repeat =True
        elif menuSelect == "3":
            print ("Co Efficient")
            #CoefficientOfDev()
            repeat = True
        elif menuSelect == "4":
            print ("Averages")
            repeat = True
        elif menuSelect == "5":
            print("menu exit")
            repeat = False
        else:
            print ("Invalid answer, please reenter")
            repeat = True
menu()