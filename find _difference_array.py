def find_defference(nums1,nums2):
    res=[]
    ans1=[]
    ans2=[]
    for x in nums1 :
        if x not in nums2 and x not in ans1:
            ans1.append(x)
    for x in nums2:
        if x not in nums1 and x not in ans2:
            ans2.append(x)
            
    res.extend((ans1,ans2))
    return res

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(find_defference(nums1,nums2))       
                    
            
  