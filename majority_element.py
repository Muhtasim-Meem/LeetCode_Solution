nums = [2,2,1,1,1,1,1,1,2,2]
mx = None
count = 0
for i in range(len(nums)):
    if count == 0:
        mx = nums[i]

    if mx == nums[i]:
        count += 1
    else:
        count -= 1

print(mx)    