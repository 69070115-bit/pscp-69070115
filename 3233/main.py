"""main"""
win = input().split()
win_char = win[0]
win_num = win[1]

my = input().split()
my_char = my[0]
my_num = my[1]

same_char = my_char == win_char
last2 = my_num[-2:] == win_num[-2:]
last3 = my_num[-3:] == win_num[-3:]

if same_char and my_num == win_num:
    prize = 1000000
elif my_num == win_num:
    prize = 100000
elif same_char and last3:
    prize = 2000
elif same_char and last2:
    prize = 1000
elif last3:
    prize = 200
elif last2:
    prize = 100
elif same_char:
    prize = 20
else:
    prize = 0

print(prize)
