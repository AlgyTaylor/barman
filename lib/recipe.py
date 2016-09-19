import yaml
import glob

# load all cocktails
def load(directory):
    datafiles = glob.glob(directory + "/*.yml")
    return list(map(loadCocktail, datafiles))

# load an individual cocktail
def loadCocktail(filename):
    f = open(filename)
    data =  yaml.safe_load(open(filename))
    f.close()
    return data

