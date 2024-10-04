def find_pivot(nums):
    n = len(nums)
    
    psum=[0]*(n+1)
    
    for i in range(len(nums)):
        psum[i+1]=psum[i]+nums[i]

    postsum=[0]*(n+1)
    
    for i in range(len(nums)-1, -1, -1):
        postsum[i]=postsum[i+1]+nums[i]
    return (psum,postsum)    


nums=[1,7,3,6,5,6]
print(find_pivot(nums))    
    