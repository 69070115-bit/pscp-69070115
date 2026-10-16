"""Resistor"""


digits = {
    "black": 0, "brown": 1, "red": 2, "orange": 3,
    "yellow": 4, "green": 5, "blue": 6, "purple": 7,
    "grey": 8, "white": 9
}

multiplier = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000,
    "yellow": 10000, "green": 100000, "blue": 1000000,
    "purple": 10000000, "gold": 0.1, "silver": 0.01
}

tolerance = {
    "brown": 0.01, "red": 0.02, "green": 0.005,
    "blue": 0.0025, "purple": 0.001, "grey": 0.0005,
    "gold": 0.05, "silver": 0.10
}

c1, c2, c3, c4 = [input().strip().lower() for _ in range(4)]

value = (digits[c1] * 10 + digits[c2]) * multiplier[c3]
tol = tolerance[c4]

print(f"{value * (1 - tol):.4f}")
print(f"{value * (1 + tol):.4f}")
