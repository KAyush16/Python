'''Question:
How can you convert a Python dictionary to a JSON string and save it to a file?

Answer:
You can use the json.dump() function to write a Python dictionary to a JSON file. Here is an example:'''
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
