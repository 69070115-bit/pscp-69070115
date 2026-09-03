"""conan"""
n= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"]
text = input()
k = int(input())

answer = ""

for ch in text:
    pos = n.index(ch)
    new_pos = (pos + k) % 26
    answer += n[new_pos]

print(answer)
