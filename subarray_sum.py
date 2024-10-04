def sub_array_sum(nums,n,left,right):
    subarray_sums = []
    n = len(nums)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            subarray_sums.append(current_sum)
    
    subarray_sums.sort()
    ans =0
    for i in range(left-1,right):
        ans += subarray_sums[i]
    return ans % 1000000007   

    



nums = [1, 2, 3, 4]

print(sub_array_sum(nums,4,1,5))