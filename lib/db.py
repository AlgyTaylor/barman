import glob
import sqlite3

def init(initDir):
    db = makeDb()
    db.row_factory = sqlite3.Row

    for sqlFile in glob.glob(initDir + "/*.sql"):
        sql = open(sqlFile, 'r')
        createDb(db, sql.read())

    return db

def makeDb():
    conn = sqlite3.connect(":memory:")
    return conn

def createDb(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchone()

def addIngredients(conn, ingredients):
    cursor = conn.cursor()
    sql = 'INSERT INTO ingredient(type, name) VALUES (?, ?)'
    cursor.executemany(sql, ingredients)

    return

def addCocktails(conn, cocktails):
    cursor = conn.cursor()
    sql = 'INSERT INTO cocktail(name, description) VALUES (?, ?)'

    cursor.executemany(sql, cocktails)

    return

def addCocktailIngredients(conn, ingredients):
    cursor = conn.cursor()
    sql = 'INSERT INTO cocktailIngredient(cocktail, ingredient) VALUES (?, ?)'
    cursor.executemany(sql, ingredients)

    return

def addCocktailCategories(conn, categories):
    cursor = conn.cursor()
    sql = 'INSERT INTO cocktailCategory(cocktail, category) VALUES (?, ?)'

    cursor.executemany(sql, categories)

    return

def addCocktailMethods(conn, methods):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sql = 'INSERT INTO method(cocktail, step, stepNumber) VALUES (?, ?, ?)'

    cursor.executemany(sql, methods)

    return

def getPossibleCocktails(conn):
    cursor = conn.cursor()
    
    sql = 'SELECT c.name, c.description,'
    sql += ' COUNT(ci.ingredient) AS ingredients,'
    sql += ' COUNT(i.name) AS inStock'
    sql += ' FROM cocktail c'
    sql += ' JOIN cocktailIngredient ci'
    sql += ' ON c.name = ci.cocktail'
    sql += ' LEFT JOIN ingredient i'
    sql += ' ON ci.ingredient = i.name'
    sql += ' GROUP BY c.name, c.description'
    sql += ' HAVING ingredients = inStock;'
    
    cursor.execute(sql)
    
    return cursor.fetchall()
