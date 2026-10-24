"""Impostor"""

import ast

members = {}

while True:
    line = input()
    if line == "Start":
        break
    members.update(ast.literal_eval(line))

dead = {}

while True:
    name = input()
    if name == "End":
        break
    if name in members:
        dead[name] = members.pop(name)

count = sum(role == "Impostor" for role in members.values())

print(f"{count} Impostor Remains")
print("***Alive***")

for name in sorted(members):
    print(f"{name} : {members[name]}")

print("***Dead***")

for name in sorted(dead):
    print(f"{name} : {dead[name]}")
