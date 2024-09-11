def reverseint(n):
    if n>2**31-1 or n<-2**31:
        return 0
    else:
        if n < 0:
            sign = -1
        else:
            sign = 1
        n=abs(n) 
    
        string=(str(n))
        reversed_string=string[::-1]
        reversed_int=int(reversed_string)
        if reversed_int>2**31-1 or reversed_int <-2**31:
            return 0
        else:
            return sign*reversed_int
    

num=120
res=reverseint(num)
print(res)
        
        
        