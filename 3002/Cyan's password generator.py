"""Cyan's password generator"""

Username = input()
Usersur = input()
Userage = input()

if len(Username) >= 5 and len(Usersur) >= 5:
    print(f"{Username[:2]}{Usersur[-1]}{Userage[-1]}")
else:
    print(f"{Username[0]}{Userage}{Usersur[-1]}")
