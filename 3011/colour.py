"""3011"""

color1 = input().strip()
color2 = input().strip()

if (color1 == "Red" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Red"):
    print("Orange")

elif (color1 == "Red" and color2 == "Blue") or (color1 == "Blue" and color2 == "Red"):
    print("Violet")

elif (color1 == "Yellow" and color2 == "Blue") or (color1 == "Blue" and color2 == "Yellow"):
    print("Green")

else:
    print("Error")
