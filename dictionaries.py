#These are the definitions out of the Scrabble dictionary

definitions = {"chicken":"TO LOSE ONE'S NERVE",
               "pig":"TO BEAR PIGS",
               "cow":"TO INTIMIDATE",
               "sheep":"A RUMINANT MAMMAL"}

definitions2 = dict(chicken="TO LOSE ONE'S NERVE",
                   pig="TO BEAR PIGS",
                   cow="TO INTIMIDATE",
                   sheep="A RUMINANT MAMMAL")

definitions3 = dict([("chicken","TO LOSE ONE'S NERVE"),
                     ("pig","TO BEAR PIGS"),
                     ("cow","TO INTIMIDATE"),
                     ("sheep","A RUMINANT MAMMAL")])

print(definitions)
print(definitions["cow"])

definition_word_len = { word: len(word) for word in definitions if word[0] == "c" }

print(definition_word_len)

assert definitions == definitions2 == definitions3
assert "pig" in definitions
assert "crow" not in definitions

definitions["crow"] = "TO BOAST"

print(definitions)

print(definition_word_len)

definitions.get("mouse","")

try:
  mouse_def = definitions["mouse"]

except:
  print("mouse not found")

for word, definition in definitions.items():
  print('{}: {}'.format(word, definition))

def_keys = [ key for key in definitions.keys() ]
#This is not the same:
def_keys2 = [ definitions.keys() ]

def_keys2 = []
for key in definitions.keys():
  def_keys2.append(key)


def_values = list(definitions.values())
print("That's all folks")