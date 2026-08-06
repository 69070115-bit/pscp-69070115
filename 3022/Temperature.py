"""Temperature"""

t = float(input())
x = input()
y = input()

if x == "C":
    if y == "K":
        print(f"{t+273.15:.2f}")
    elif y == "F":
        print(f"{t*9/5+32:.2f}")
    elif y == "R":
        print(f"{(t+273.15)*9/5:.2f}")
    else:
        print(float(t))
elif x == "K":
    if y == "C":
        print(f"{t-273.15:.2f}")
    elif y == "F":
        print(f"{(t-273.15)*9/5+32:.2f}")
    elif y == "R":
        print(f"{t*9/5:.2f}")
    else:
        print(float(t))
elif x == "F":
    if y == "C":
        print(f"{(t - 32)*5/9:.2f}")
    elif y == "K":
        print(f"{((t - 32)*5/9)+273.15:.2f}")
    elif y == "R":
        print(f"{(((t - 32)*5/9)+273.15)*9/5:.2f}")
    else:
        print(float(t))
elif x == "R":
    if y == "C":
        print(f"{(t - 491.67) * 5 / 9:.2f}")
    elif y == "K":
        print(f"{((t - 491.67) * 5 / 9)+273.15:.2f}")
    elif y == "F":
        print(f"{((t - 491.67) * 5 / 9)*9/5+32:.2f}")
    else:
        print(float(t))
else:
    print(float(t))
