import random

categories = ["numbers","upperCase","spaces","specialCHaracters","minimumTwo"]

charDef = {
    "default":[[97,123]],
    "numbers":[[48,58]],
    "upperCase":[[65,90]],
    "spaces":[[32,33]],
    "specialCharacters":[[33,48],[58,65],[91,96],[123,127]],
    "minimumTwo": [[]]
}

password = {
    "length": 22,
    "include": {
        "numbers": True,
        "upperCase": True,
        "spaces":True,
        "specialCharacters": True,
        "minimumTwo": False #minimum 2 of each included char type
    },
    "charCount": {
      "default": 0
    }
}

options = list(range(charDef["default"][0][0],charDef["default"][0][1]))

for x,y in password["include"].items():
    if y == True:
        password["charCount"][x] = 0
        a = charDef[x]
        for b in a:
          options += list(range(b[0],b[1]))

zzz = ""
for c in range(password["length"]):
  zzz += chr(random.choice(options))
print(zzz)
