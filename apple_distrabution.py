nums1=[1,3,2]
nums2=[4,3,1,5,2]
nums2.sort(reverse=True)
capacity = 0
x=sum(nums1)
count=0
for i in nums2:
    if x > capacity:
        capacity+=i
        count+=1
    
print(capacity,count)        
    
    