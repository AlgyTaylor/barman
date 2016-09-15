import yaml

def prepForDatabase(cocktails):
    array = []

    for cocktail in cocktails:
        for ingredient in cocktail['ingredients']:
            array.insert(len(array), (cocktail['name'], ingredient))

    return array
