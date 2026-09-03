"""idk"""
N = int(input())
list_num = []
text = ""

for i in range(N):
    num1 = int(input())
    num2 = int(input())

    if num1 > num2:
        list_num.append(num1)
    else:
        list_num.append(num2)

for i, num in enumerate(list_num):
    if i == len(list_num) - 1:
        text += str(num)
    else:
        text += str(num) + " " + "+" + " "

total = 0
for num in list_num:
    total += num

if N == 1:
    print(text)
else:
    print(text + " = " + str(total))
