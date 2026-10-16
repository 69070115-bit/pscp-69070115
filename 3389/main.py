"""Smart Trash Collector"""
n = int(input())

for _ in range(n):
    plastic, can, glass = map(float, input().split())
    total = plastic + can + glass
    result = []

    if total > 50:
        result.append("Overloaded")

    for name, value in [
        ("Plastic", plastic),
        ("Can", can),
        ("Glass", glass)
    ]:
        if value > 20:
            result.append(f"Check Type {name}")

    print(f"{total:.1f}", end="")
    if result:
        print(", " + ", ".join(result))
    else:
        print()
