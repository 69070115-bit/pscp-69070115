"""มาเป็นทีม"""
N, M = map(int, input().split())

if not (1 <= N <= 10 and 1 <= M <= 20):
    print("Data Incorrect")
else:
    teams = []
    valid = True

    for i in range(N):
        scores = list(map(int, input().split()))

        if len(scores) != M or any(s < 0 or s > 100 for s in scores):
            valid = False

        teams.append(scores)

    if not valid:
        print("Data Incorrect")
    else:
        total = 0

        for i, scores in enumerate(teams, start=1):
            avg = sum(scores) / M
            maximum = max(scores)
            total += sum(scores)

            print(f"Team {i}: Average = {avg:.2f}, Max = {maximum}")

        print(f"Total Score of All Teams = {total}")
