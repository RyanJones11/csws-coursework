import csv
def keywordSearch():
    data = []
    searchResults = []

    with open("dataset.csv") as csvfile:#'dataset.csv' to be replaced with the final filename of the dataset
        reader = csv.reader(csvfile)
        for row in reader:#Reads each row of the CSV file
            data.append(row)

    searchTerm = input("Please enter a search term:\n")#Takes the users input to be used as a keyword to search

    for i in range(0,(len(row) - 4)):#Used to only search the columns that contain searchable data.
        column = [x[i] for x in data]
        if searchTerm in column:
            for x in range(0,len(data)):
                if searchTerm == data[x][i]:#This compares the input to the individual value of each "cell" in the CSV file in the data List
                    searchResults.append(data[x])
                    print(searchResults)#Outputs the collected rows that contain the search term.
                    
    if len(searchResults) == 0:
        print("Error:\nNo results match \"" + searchTerm +"\"") #If the searchResults list is empty then an error message is outputted
keywordSearch()