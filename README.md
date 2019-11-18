# ProgMenu

> A lil library to help with cmd line flags and stuff

> YES I KNOW ONE EXISTS I WROTE THIS THEN LEARNED ABOUT argparse

## Installation

- Clone it and use it like any other library (?)

## Usage

> Add this code to the main file to test if it's working:

```
from progMenu import printFAA
printFAA()
```

> The `printFAA` function prints all the passed flags, assigned, and args in that order

- A *flag* is: `-f or --flag`
- An *assigned* is a flag with an associated arg: `-s 12` or `--seed=12`
- An *arg* is pretty much anything else: `$ cmd -s <arg> <lonelyArg>`

> You can create MenuEntry objects which can be used to run a function when the script starts:

- In the main file:
```
from progMenu import menu
from menuEntries import *
PARSER=menu.parse(True)  #True means run the functions instead of just returning if the entry was called
print(f"PARSER: {PARSER}")  #Just so you can see what PARSER is. It's a dictionary of the entry names and what they returned (if called in the cmd line)
```

- In another file containing the entries (in this case named `menuEntries.py`):
```
from progMenu import MenuEntry
def aFunc():
	print("This is an entry function!")
	return True

a=MenuEntry("entryName", ['f', "flag"], aFunc, 0)  #help(MenuEntry) for more details)
```

- Now when you run the main file without using `f` or `flag` as a flag, nothing will happen. But if you do, it prints "This is an entry function!"

