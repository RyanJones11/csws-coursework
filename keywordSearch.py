import csv
def keywordSearch():
    data = []
    searchResults = []
    with open("dataset.csv") as csvfile:#'dataset.csv' to be replaced with the final filename of the dataset
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    searchTerm = input("Please enter a search term:\n")
    for i in range(0,(len(row) - 4)):
        column = [x[i] for x in data]
        if searchTerm in column:
            for x in range(0,len(data)):
                if searchTerm == data[x][i]:
                    searchResults.append(data[x])
                    print(searchResults)
    if len(searchResults) == 0:
        print("Error no results match \"" + searchTerm +"\"")
keywordSearch()