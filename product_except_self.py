class Solution(object):
    def productExceptSelf( nums):
        
        x=len(nums)
        n=(len(nums)+1) 
        res=[1]*n
        pref=1
        
        for i in range(len(nums)):
            res[i+1]=pref*nums[i]
            print(res)
            pref*=nums[i]
            print(res)
        
        
        postf=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postf
            postf*=nums[i]
        return res [:x]   
        
    lst=[1,2,3,4]
    print(productExceptSelf(lst))        