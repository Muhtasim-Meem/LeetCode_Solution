nums = [1,2,3,1]
k=3

for i in range(len(nums) - 1, 0, -1):
    if nums[i] ==nums[i-1]:
        print(i,i-1)
    