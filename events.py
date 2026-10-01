import os
import json
from shutil import rmtree

class Datapackinator:

    def __init__(self, name, description, namespace, delete = True):
        self.namespace = namespace
        self.pack_path = os.path.join(os.path.abspath(os.getcwd()), name)
        self.delete = delete
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
        with open(os.path.join(self.pack_path, "pack.mcmeta"), "w") as pack:
            pack.write(json.dumps(mcmeta, indent = 4))

        if self.delete & os.path.exists(os.path.join(self.pack_path, "data")):
            rmtree(os.path.join(self.pack_path, "data"))

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace), exist_ok=True)

    def shapeless(self, ingredients, result, count, id, subfolder = ""):
        ingredients_list = []

        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if ingredient.find("#") == -1:
                    ingredients_list.append({"item": ingredient})
                else:
                    ingredients_list.append({"tag": ingredient})
        else:
            if ingredients.find("#") == -1:
                ingredients_list.append({"item": ingredients})
            else:
                ingredients_list.append({"tag": ingredients})
        
        structure = {
            "type": "minecraft:crafting_shapeless",
            "ingredients": ingredients_list,
            "result": {
                "id": result,
                "count": count
            }
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder, id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def shaped(self, ingredients, pattern, result, count, id, subfolder = ""):
        ingredients_dict = {}
        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if str(ingredient.keys()).find("#") == -1:
                    ingredients_dict.setdefault(next(iter(ingredient.values())), {"item": next(iter(ingredient.keys()))})
                else:
                    ingredients_dict.setdefault(next(iter(ingredient.values())), {"tag": next(iter(ingredient.keys()))})
        else:
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

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder, id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def stonecutting(self, ingredients, result, count, id, subfolder = ""):
        ingredient_json = {}

        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if ingredient.find("#") == -1:
                    ingredient_json = {"item": ingredient}
                else:
                    ingredient_json = {"tag": ingredient}
        else:
            if ingredients.find("#") == -1:
                ingredient_json = {"item": ingredients}
            else:
                ingredient_json = {"tag": ingredients}
        
        structure = {
            "type": "minecraft:stonecutting",
            "ingredient": ingredient_json,
            "result": {
                "id": result,
                "count": count
            }
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder, id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def smelting(self, ingredients, result, id, experience = 0, cookingtime = 200, subfolder = ""):
        ingredient_json = {}

        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if ingredient.find("#") == -1:
                    ingredient_json = {"item": ingredient}
                else:
                    ingredient_json = {"tag": ingredient}
        else:
            if ingredients.find("#") == -1:
                ingredient_json = {"item": ingredients}
            else:
                ingredient_json = {"tag": ingredients}

        structure = {
            "type": "minecraft:smelting",
            "ingredient": ingredient_json,
            "result": {
                "id": result
            },
            "experience": experience,
            "cookingtime": cookingtime
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder, id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def blasting(self, ingredients, result, id, experience = 0, cookingtime = 200, subfolder = ""):
        ingredient_json = {}

        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if ingredient.find("#") == -1:
                    ingredient_json = {"item": ingredient}
                else:
                    ingredient_json = {"tag": ingredient}
        else:
            if ingredients.find("#") == -1:
                ingredient_json = {"item": ingredients}
            else:
                ingredient_json = {"tag": ingredients}

        structure = {
            "type": "minecraft:blasting",
            "ingredient": ingredient_json,
            "result": {
                "id": result
            },
            "experience": experience,
            "cookingtime": cookingtime
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder, id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def smoking(self, ingredients, result, id, experience = 0, cookingtime = 200, subfolder = ""):
        ingredient_json = {}

        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if ingredient.find("#") == -1:
                    ingredient_json = {"item": ingredient}
                else:
                    ingredient_json = {"tag": ingredient}
        else:
            if ingredients.find("#") == -1:
                ingredient_json = {"item": ingredients}
            else:
                ingredient_json = {"tag": ingredients}

        structure = {
            "type": "minecraft:smoking",
            "ingredient": ingredient_json,
            "result": {
                "id": result
            },
            "experience": experience,
            "cookingtime": cookingtime
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder, id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def campfire_cooking(self, ingredients, result, id, experience = 0, cookingtime = 200, subfolder = ""):
        ingredient_json = {}

        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if ingredient.find("#") == -1:
                    ingredient_json = {"item": ingredient}
                else:
                    ingredient_json = {"tag": ingredient}
        else:
            if ingredients.find("#") == -1:
                ingredient_json = {"item": ingredients}
            else:
                ingredient_json = {"tag": ingredients}

        structure = {
            "type": "minecraft:campfire_cooking",
            "ingredient": ingredient_json,
            "result": {
                "id": result
            },
            "experience": experience,
            "cookingtime": cookingtime
        }

        if not os.path.exists(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", self.namespace, "recipe", subfolder, id + ".json"), "w") as file:
            file.write(json.dumps(structure, indent=4))

    def remove(self, id, subfolder = ""):
        namespace = id[0 : id.find(":")]
        recipe = id[id.find(":") + 1 : len(id)]
        
        if not os.path.exists(os.path.join(self.pack_path, "data", namespace, "recipe", subfolder)):
            os.makedirs(os.path.join(self.pack_path, "data", namespace, "recipe", subfolder), exist_ok=True)
        with open(os.path.join(self.pack_path, "data", namespace, "recipe", subfolder, recipe + ".json"), "w") as file:
            file.write(json.dumps({}, indent=4))

    