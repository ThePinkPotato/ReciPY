# ReciPY

ReciPY is a "tool" that lets you script recipe changes for datapacks. It's super simple to use. Yay.

To use it, place the `events.py` file in any folder, and then create a new python file with the following code 
```
from events import Datapackinator 
pack = Datapackinator(pack name, namespace, description)
```
Be sure to fill out the arguments as necessary. Now you can start scripting!

To finally generate your datapack, simply run the python file, and the datpack will be output in the same folder as the `events.py` file. Changing your script *should* change your datapack files automatically when you run the program again.

ReciPY is far from feature complete, with plans to support recipe types past 1.21.1, add datapack support, and a few quality of life features, such as automatic file deletion.