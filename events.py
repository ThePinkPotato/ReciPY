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

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace), exist_ok=True)

        for x, ingredient in enumerate(ingredients):
            if ingredient.find("#") == -1:
                if x != len(ingredients):
                    ingredient_json = {"item": ingredient}
                    ingredients_list.append(ingredient_json)
                else:
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

