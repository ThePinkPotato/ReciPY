import os
import json

class Datapackinator:

    def __init__(self, name, description, namespace):
        self.namespace = namespace
        self.pack_path = os.path.join(os.path.abspath(os.getcwd()), name)
        mcmeta = {
            "pack": {
                "description": description,
                "supported_formats": [
                    48,
                    48
                ]
            }
        }
        if not os.path.exists(self.pack_path):
            os.mkdir(self.pack_path)
        with open(os.path.join(self.pack_path, "pack.mcmeta"), "w") as file:
            file.write(json.dumps(mcmeta, indent = 4))

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace), exist_ok=True)

    def shapeless(self, ingredients, result, count, id):
        ingredients_list = []

        for ingredient in ingredients:
            if ingredient.find("#") == -1:
                ingredient_json = {"item": ingredient}
                ingredients_list.append(ingredient_json)
            else:
                ingredient_json = {"tag": ingredient}
                ingredients_list.append(ingredient_json)
        
        structure = {
            "type": "minecraft:crafting_shapeless",
            "ingredients": ingredients_list,
            "result": {
                "id": result,
                "count": count
            }
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe")):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe"), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def shaped(self, ingredients, pattern, result, count, id):
        ingredients_dict = {}

        for ingredient in ingredients:
            if str(ingredient.keys()).find("#") == -1:
                ingredients_dict.setdefault(next(iter(ingredient.values())), {"item": next(iter(ingredient.keys()))})
            else:
                ingredients_dict.setdefault(next(iter(ingredient.values())), {"tag": next(iter(ingredient.keys()))})

        structure = {
            "type": "minecraft:crafting_shaped",
            "pattern": pattern,
            "key": ingredients_dict,
            "result": {
                "id": result,
                "count": count
            }
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe")):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe"), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def stonecutting(self, ingredient, result, count, id):
        ingredient_json = {}
        if ingredient.find("#") == -1:
            ingredient_json = {"item": ingredient}
        else:
            ingredient_json = {"tag": ingredient}
        
        structure = {
            "type": "minecraft:stonecutting",
            "ingredient": ingredient_json,
            "result": {
                "id": result,
                "count": count
            }
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe")):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe"), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))