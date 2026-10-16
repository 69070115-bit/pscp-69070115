"""นักล่าอสูร"""
demons = {
    "Spider Demon": 1,
    "Swamp Demon": 2,
    "Arrow Demon": 1,
    "Hand Demon": 2,
    "Drum Demon": 3,
    "Mugen Train": 2,
    "Upper Moon": 3
}

total = 0
kills = 0

while kills < 5:
    demon = input().strip()

    if demon not in demons:
        continue

    # โจมตีด้วยจำนวนที่คาดเดาไว้
    attack = demons[demon]
    print(attack, flush=True)
    total += 1

    # อ่านผลลัพธ์จากระบบ
    result = input().strip()

    if result == "kill":
        kills += 1
    elif result == "back":
        continue

print(total)
