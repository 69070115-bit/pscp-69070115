"""saitama"""
import math

push_up_goal = int(input())
sit_up_goal = int(input())
squat_goal = int(input())
run_goal = int(input())
push_up_do = int(input())
sit_up_do = int(input())
run_do = int(input())
squat_do = int(input())

push_up_sum = math.ceil(push_up_goal / push_up_do)
sit_up_sum = math.ceil(sit_up_goal / sit_up_do)
squat_sum = math.ceil(squat_goal / squat_do)
run_sum = math.ceil(run_goal / run_do)

goal = max(push_up_sum, sit_up_sum, squat_sum, run_sum)
print(goal)
