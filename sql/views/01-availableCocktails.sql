CREATE VIEW main.availableCocktail AS
    SELECT name, description
    FROM (
        SELECT c.name, c.description,
            COUNT(ci.ingredient) AS ingredients,
            COUNT(i.name) AS inStock
         FROM cocktail c
         JOIN cocktailIngredient ci
           ON c.name = ci.cocktail
         LEFT JOIN ingredient i
           ON ci.ingredient = i.name
         GROUP BY c.name, c.description
         HAVING ingredients = inStock
    ) availableCocktail;
