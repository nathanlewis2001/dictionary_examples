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

definition_word_len = { word: len(word) for word in definitions }

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

def_keys = [ definitions.keys() ]

def_values = list(definitions.values())