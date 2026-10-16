"""FourDirections"""

s = input()

U = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
D = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
L = ["  *  ", " *   ", "*****", " *   ", "  *  "]
R = ["  *  ", "   * ", "*****", "   * ", "  *  "]

arrows = {'U': U, 'D': D, 'L': L, 'R': R}

for i in range(5):
    print(" ".join(arrows[c][i] for c in s))
