from parsers.recipe import WpJsonRecipe

<<<<<<< HEAD:parsers/minimalistbaker.py
class Minimalistbaker(WpJsonRecipe):
=======
from .recipe import Recipe

class Minimalistbaker(Recipe):
>>>>>>> 257c167 (Updated the project to be a python package):plainoldrecipe/parsers/minimalistbaker.py

    def get_json_recipe(self, d):
        recipe = super().get_json_recipe(d)
        # thewoksoflife.com for some reason has double parentheses in its
        # ingredients. Remove them.
        recipe['ingredients'] = [
                ingredient.replace('((', '(').replace('))', ')').replace('//', '/')
                for ingredient in recipe.get('ingredients', [])]
        return recipe
