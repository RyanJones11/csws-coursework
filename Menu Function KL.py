def menu():
    repeat=True
    while repeat==True:
        menuSelect=0
        print("Enter a number between 1-4: ")
        menuSelect=input()
        if menuSelect == "1":
            print("option 1")
            repeat = False
        elif menuSelect == "2":
            print ("option 2")
            repeat =False
        elif menuSelect == "3":
            print ("option 3")
            repeat = False
        elif menuSelect == "4":
            print ("option 4")
            repeat = False
        else:
            print ("Invalid answer, please reenter")
            repeat = True
menu()