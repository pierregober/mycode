#!/usr/bin/env python3
marvelchars= {
"Starlord":
  {"real name": "Peter Quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "Raven Darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "Jennifer Walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }

print("[0]: Starlord")
print("[1]: Mystique")
print("[2]: She-Hulk")
char_name = input("Which character do you want to know about? [0 to 2]: " )

selectedChar = ""

if(char_name == "0"):
    selectedChar = "Starlord"
if(char_name == "1"):
    selectedChar = "Mystique"
if(char_name == "2"):
    selectedChar = "She-Hulk"
else:
    print("pierre figure this out with regex")

print("[0]: real name")
print("[1]: powers")
print("[2]: archenemy")
char_stat = input(" What statistic do you want to know about? [0 to 2]: ")

selectedStatName = ""

if(char_stat == "0"):
    selectedStatName = "real name"
if(char_stat == "1"):
    selectedStatName = "powers"
if(char_stat == "2"):
    selectedStatName = "archenemy"
else:
    print("pierre figure this out with regex")
    
test = ""

for key, value in marvelchars[selectedChar]:
    if(key == selectedStatName):
        test = value
    
print(selectedChar + "'s " + selectedStatName + "is:" + test)
