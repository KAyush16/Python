import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

# serializing jason 
json_object = json.dumps(languages, indent=4)

# writing samples to sample.json
with open("sample.json","w") as outfile:
    outfile.write(json_object)
    
    
print(type(json_object))