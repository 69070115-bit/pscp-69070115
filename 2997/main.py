"""Elo"""

Ra = int(input())
Rb = int(input())
AB = str(input())

EA = 1 / (1 + 10 ** ((Rb - Ra) / 400))
EB = 1 / (1 + 10 ** ((Ra - Rb) / 400))

if AB == "A":
    print(f"{EA:.2f}")
elif AB == "B":
    print(f"{EB:.2f}")
