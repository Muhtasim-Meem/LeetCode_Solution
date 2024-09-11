def substring(strin_g):
    n=len(strin_g)
    substrings=[]
    for i in range(n):
        for j in range(i+1,n+1):
            substrings.append(strin_g[i:j])
    for x in substrings:
        if len(x)==1:
            substrings.remove(x)       
    return substrings 

def reverse(substrings):
    reversed_substrings=[]
    for sub in lst:
        reversed_substrings.append(sub[::-1])
    return reversed_substrings 

def palindrome(strin_g,substrings):
    pal=[]
    for x in strin_g:
        for y in substrings:
            if x == y:
                pal.append(y)
    long_palin=pal[0]            
    for i in range(1,len(pal)):
        if len(pal[i]) > len(long_palin):
            long_palin=pal[i]
    return long_palin        
        

string="bbb"
lst=substring(string) 
ls1=reverse(lst)
res=palindrome(lst,ls1)
print(res)