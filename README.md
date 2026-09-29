# ReciPY

ReciPY is a "tool" that lets you script recipe changes for datapacks. It's super simple to use. Yay.

To use it, place the `events.py` file in any folder, and then create a new python file with the line `from events import Datapackinator`. From there, simply type `pack = Datapackinator(pack name, namespace, description)` to initiate the pack, with all of the arguments filled in to your needs. Then you can start scripting!

ReciPY is far from feature complete, with plans to support recipe types past 1.21.1, add datapack support, and a few quality of life features, such as automatic file deletion.

### Supported Recipe Types & Arguments

`shapeless(ingredients, result, count, id)`
- `ingredients` is the ingredients in the recipe, in list form
- `result` is the result of the recipe
- `count` is the amount the recipe outputs
- `id` is the id of the recipe, what the file will be saved as (do not have duplicates)

`shaped(ingredients, pattern, result, count, id)`
- `ingredients` is the ingredients of the recipe, in a list, with form `{ingredient, key}`
- `pattern` is the recipe pattern, using the keys established in the previous arguments, in list form
- `result` is the result of the recipe
- `count` is the amount the recipe outputs
- `id` is the id of the recipe, what the file will be saved as (do not have duplicates)

`stonecutting(ingredient, result, count, id)`
- `ingredient` is the ingredient of the recipe
- `result` is the result of the recipe
- `count` is the amount the recipe outputs
- `id` is the id of the recipe, what the file will be saved as (do not have duplicates)

`smelting(ingredient, result, id, (experience), (cookingtime))`
- `ingredient` is the ingredient of the recipe
- `result` is the result of the recipe
- `count` is the amount the recipe outputs
- `id` is the id of the recipe, what the file will be saved as (do not have duplicates)
- `experience` is an optional argument, how much experience the player will gain from the recipe
- `cookingtime` is an optional argumetn, how long the recipe will take, in ticks (default is 200, or 10 seconds)

`blasting(ingredient, result, id, (experience), (cookingtime))`
- `ingredient` is the ingredient of the recipe
- `result` is the result of the recipe
- `count` is the amount the recipe outputs
- `id` is the id of the recipe, what the file will be saved as (do not have duplicates)
- `experience` is an optional argument, how much experience the player will gain from the recipe
- `cookingtime` is an optional argumetn, how long the recipe will take, in ticks (default is 200, or 10 seconds)

`smoking(ingredient, result, id, (experience), (cookingtime))`
- `ingredient` is the ingredient of the recipe
- `result` is the result of the recipe
- `count` is the amount the recipe outputs
- `id` is the id of the recipe, what the file will be saved as (do not have duplicates)
- `experience` is an optional argument, how much experience the player will gain from the recipe
- `cookingtime` is an optional argumetn, how long the recipe will take, in ticks (default is 200, or 10 seconds)

`campfire_cooking(ingredient, result, id, (experience), (cookingtime))`
- `ingredient` is the ingredient of the recipe
- `result` is the result of the recipe
- `count` is the amount the recipe outputs
- `id` is the id of the recipe, what the file will be saved as (do not have duplicates)
- `experience` is an optional argument, how much experience the player will gain from the recipe
- `cookingtime` is an optional argumetn, how long the recipe will take, in ticks (default is 200, or 10 seconds)