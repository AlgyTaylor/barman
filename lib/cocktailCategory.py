def prepForDatabase(cocktails):
    array = []

    for cocktail in cocktails:
        for category in cocktail['categories']:
            array.insert(len(array), (cocktail['name'], category))

    return array
