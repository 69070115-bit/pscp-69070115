"""Shorten"""
nums = []

while True:
    n = int(input())
    if n == -1:
        break
    nums.append(n)

if nums:
    result = []
    start = prev = nums[0]

    for n in nums[1:]:
        if n == prev + 1:
            prev = n
        else:
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = prev = n

    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")

    print(", ".join(result))
else:
    print("")
