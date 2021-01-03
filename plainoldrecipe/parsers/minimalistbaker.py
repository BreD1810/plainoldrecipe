from .recipe import WpJsonRecipe

class Minimalistbaker(WpJsonRecipe):

    def get_json_recipe(self, d):
        recipe = super().get_json_recipe(d)
        # thewoksoflife.com for some reason has double parentheses in its
        # ingredients. Remove them.
        recipe['ingredients'] = [
                ingredient.replace('((', '(').replace('))', ')').replace('//', '/')
                for ingredient in recipe.get('ingredients', [])]
        return recipe
