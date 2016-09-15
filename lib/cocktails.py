import yaml

def load(filename):
    f = open(filename)
    data = yaml.safe_load(f)
    f.close()

    return data

def prepForDatabase(cocktails):
    array = []

    for cocktail in cocktails:
        array.insert(len(array), (cocktail['name'], cocktail['description']))

    return array
