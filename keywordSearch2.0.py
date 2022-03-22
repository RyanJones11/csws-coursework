import pandas as pd

def keywordSearch():
    data = pd.read_csv("dataset.csv")
    searchResults = []

    searchTerm = input("Please enter your search term: \n")
    if searchTerm in data:
        

        print(searchResults)
    else:
        print("ERROR\nInvalid search term...")

keywordSearch()