
nums = [1,7,3,6,5,6]
total = 0
if sum(nums) % 2 == 0:
    for num in nums:
        if total < (sum(nums))/2:
            total += num
    print(total)
else:
    print(-1)



