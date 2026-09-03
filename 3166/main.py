"""pass or fail """
N = int(input())
total_score = 0
fail_count = 0
for _ in range(N):
    score = int(input())
    total_score += score
    if score < 50:
        fail_count += 1
avg = total_score / N
print(f"{avg:.1f}")
if not fail_count and avg >= 60.0:
    print("PASS")
else:
    print("FAIL")
