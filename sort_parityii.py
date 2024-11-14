lst=[4,2,5,7]
n=len(lst)
nums=[]

for i in range(len(lst)-1,-1,-1):
    if lst[i]%2==0:
        nums.append(lst[i])
        lst.pop(i)
print(lst,nums) 

 
res=[]
for i in range(2):
    res.append(nums[i])
    res.append(lst[i])
print(res)    