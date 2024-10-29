nums = [1,1,0,1,1,1,1,0,0,0,1,1,1]

count = 0
mx = 0
for i in range(len(nums)):
    
    
    if nums[i] == 1:
        count += 1
    else: 
        count = 0

    if count > mx:
        mx = count    
print(mx)        
        