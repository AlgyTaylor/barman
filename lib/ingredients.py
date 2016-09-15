import yaml

def load(filename):
    f = open(filename)
    data = yaml.safe_load(f)
    f.close()

    return data

def prepForDatabase(data):
    array = []

    for key in data.keys():
        for value in data[key]:
            array.insert(len(array), (key, value))

    return array
