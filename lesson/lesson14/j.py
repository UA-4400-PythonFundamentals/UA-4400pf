import json



data =  """
{
"firstName": "Ivan", "lastName": "King",
"hobbies": ["reading", "traveling", "singing"],
"age": 33,
"children":
[
{
"firstName": "Vira",
"age":
3
},{
"firstName": "Maksym",
"age":
5
}
]
}
"""
user = json.loads(data)
print(user)
print(user["firstName"])

with open("lesson\\lesson14\\in.json") as file:
    user2 = json.load(file)
print(user2)
print(user2["firstName"])

user2["age"] = 99
user2["children"][0]["age"] = 33

from pprint import pprint
pprint(user2)

text = json.dumps(user2)
print(text)

with open("lesson\\lesson14\\out.json", "w") as file:
    json.dump(user2, file)

