import yaml

def load(filename):
    f = open(filename)
    data = yaml.safe_load(f)
    f.close()

    return data

def prepForDatabase(cocktails):
    cocktailList = []

    for cocktail in cocktails:
        cocktailList.insert(len(cocktailList), (cocktail['name'], cocktail['description']))
    
    return cocktailList
