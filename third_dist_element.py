nums = [1,1,2]
nums.sort()
if len(nums) > 2:
    x=max(nums)
    for j in nums:
        if j==x:
            while j in nums:
                nums.remove(j)   
    y= max(nums)
    

    for i in nums:
        if i==y:
            while i in nums:
                nums.remove(i)
                
    z=0        
    if len(nums)==0:
        print(x)
    else:    
        z=max(nums)
        print(z)

else:
    print(max(nums))

