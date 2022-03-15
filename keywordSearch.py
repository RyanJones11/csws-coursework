import csv
def keywordSearch():
    data = []
    with open("dataset.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    searchTerm = input("Please enter a search term:\n")
    for i in range(0,(len(row) - 4)):
        column = [x[i] for x in data]
        #print(column)
        if searchTerm in column:
            for x in range(0,len(data)):
                if searchTerm == data[x][i]:
                    print(data[x])
        else:
            print("Error search term not found...")
keywordSearch()