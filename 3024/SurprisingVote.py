"""SurprisingVote"""

sum_score = float(input())
max_score = float(input())

min_score = max(0, sum_score - (2*max_score))

if max_score - min_score > 2:
    print("Surprising")
else:
    print("Not surprising")
