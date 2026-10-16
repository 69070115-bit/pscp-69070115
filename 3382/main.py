"""Day08-0_02-Backward"""

data = []

while True:
    text = input()
    if text == "NULL":
        break
    data.append(text)

for text in reversed(data):
    print(text)
