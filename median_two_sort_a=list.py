def median(nums1,nums2):
    
    if not nums1 and not nums2: 
        return 0
    else:
        nums1.extend(nums2) 
        nums1.sort()
        
        n=len(nums1)
        
        if n==1:
            return nums1[0]
        
        elif n%2!=0:
            return nums1[(n//2)]
        else:
            
            x=(n/2)-1
            y=x+1
            res=float(x+y)/2
            return res  
 
 
# implement main function         