"""Decoder"""
key = input()
room = ""

floors = ["9", "10", "11", "12", "14"]

for i in range(5):
    if int(key[i]) > 5:
        room += floors[i]
        break
else:
    room += "13"

palindrome = key == key[::-1]

if palindrome:
    checks = [
        int(key[0]) + int(key[4]) > 5,
        int(key[1]) * int(key[3]) > 5
    ]
else:
    divisor = int(key[4]) or 1
    checks = [
        int(key[0]) // divisor > 5,
        int(key[1]) - int(key[4]) > 5
    ]

if checks[0]:
    room += "1"
elif checks[1]:
    room += "2"
else:
    room += "0"

total = sum(map(int, key))
product = 1

for digit in key:
    product *= int(digit)

if total > 25:
    room += "1"
elif product > 55:
    room += "2"
else:
    room += "0"

print(room)
