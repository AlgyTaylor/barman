#!/usr/bin/python

from lib import recipe
from lib import ingredients
from lib import cocktails
from lib import cocktailIngredients
from lib import cocktailCategory
from lib import method
from lib import db

print("Welcome to Barman!\n")

database = db.init("sql/create")

db.addIngredients(
    database,
    ingredients.prepForDatabase(ingredients.load("data/ingredients.yml"))
)

recipes = recipe.load("data/recipes")

db.addCocktails(
    database,
    cocktails.prepForDatabase(recipes)
)

db.addCocktailIngredients(
    database,
    cocktailIngredients.prepForDatabase(recipes)
)

db.addCocktailCategories(
    database,
    cocktailCategory.prepForDatabase(recipes)
)

db.addCocktailMethods(
    database,
    method.prepForDatabase(recipes)
)

cocktails = db.getPossibleCocktails(database)

print ("Menu\n----")
for cocktail in cocktails:
    print cocktail['name']
    print "\t" + cocktail['description']
