def prepForDatabase(cocktails):
    array = []

    for cocktail in cocktails:
        i = 1;
        for method in cocktail['method']:
            array.insert(len(array), (cocktail['name'], method, i))
            i = i + 1

    return array
