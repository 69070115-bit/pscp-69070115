"""cafe"""
day = int(input())
income_logs = []

for _ in range(day):
    income = int(input())
    income_logs.append(income)

print(sum(income_logs))
print(max(income_logs))
print(min(income_logs))
print(f"{(sum(income_logs) / len(income_logs)):.1f}")
