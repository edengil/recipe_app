
import requests
from DB.queries.queries import get_all_gluten_or_dairy_types




# a = {
#     "idMeal": "52792",
#     "title": "Bread and Butter Pudding",
#     "strDrinkAlternate": "null",
#     "strCategory": "Dessert",
#     "strArea": "British",
#     "strInstructions": "Grease a 1 litre/2 pint pie dish with butter. Cut the crusts off the bread. Spread each slice with on one side with butter, then cut into triangles. Arrange a layer of bread, buttered-side up, in the bottom of the dish, then add a layer of sultanas. Sprinkle with a little cinnamon, then repeat the layers of bread and sultanas, sprinkling with cinnamon, until you have used up all of the bread. Finish with a layer of bread, then set aside. Gently warm the milk and cream in a pan over a low heat to scalding point. Don't let it boil. Crack the eggs into a bowl, add three quarters of the sugar and lightly whisk until pale. Add the warm milk and cream mixture and stir well, then strain the custard into a bowl. Pour the custard over the prepared bread layers and sprinkle with nutmeg and the remaining sugar and leave to stand for 30 minutes. Preheat the oven to 180C/355F/Gas 4. Place the dish into the oven and bake for 30-40 minutes, or until the custard has set and the top is golden-brown.",
#     "thumbnail": "https://www.themealdb.com/images/media/meals/xqwwpy1483908697.jpg",
#     "strTags": "Pudding,Brunch",
#     "href": "https://www.youtube.com/watch?v=Vz5W1-BmOE4",
#     "ingredients": [
#             "butter",
#             "bread",
#             "sultanas",
#             "cinnamon",
#             "milk",
#             "double cream",
#             "eggs",
#             "sugar",
#             "nutmeg"
#     ],
#     "hasGluten": "False",
#     "hasDairy": "False"
# }


def hasGluten(recipe):
    includ_gluten = False
    gluten_types = get_all_gluten_or_dairy_types("gluten")

    gluten_types = [name.lower() for name in gluten_types]
    ingredients = [name.lower() for name in recipe["ingredients"]]

    for gluten in gluten_types:
        if gluten in ingredients:
            includ_gluten = True
    return includ_gluten




def hasDairy(recipe):
    includ_dairy = False
    dairy_types = get_all_gluten_or_dairy_types("dairy")
    dairy_types = [name.lower() for name in dairy_types]
    ingredients = [name.lower() for name in recipe["ingredients"]]
    for dairy in dairy_types:
        if dairy in ingredients:
            includ_dairy = True
    return includ_dairy


def get_recipes_by_ingredient(ingredient):
    recipes_response = requests.get(
        f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}"
    ).json()["results"]
    return recipes_response
