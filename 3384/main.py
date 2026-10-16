"""PickThem"""
import json

data = json.loads(input())
even = []


def find_even(items):
    for item in items:
        if isinstance(item, list):
            find_even(item)
        elif type(item) is int and item % 2 == 0:
            even.append(item)


find_even(data)
print(*even, sep="\n") if even else print("Nope")
