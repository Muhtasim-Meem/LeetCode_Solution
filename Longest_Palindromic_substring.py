def substring(strin_g):
    n=len(strin_g)
    substrings=[]
    for i in range(n):
        for j in range(i+1,n+1):
            substrings.append(strin_g[i:j])
    for x in substrings:
        if len(x)==1:
            substrings.remove(x)   
    
    reversed_substrings=[]
    for sub in substrings:
        reversed_substrings.append(sub[::-1])
    
    pal=[] 
    
    for i in range(min(len(reversed_substrings),len(substrings))) :
        if reversed_substrings[i]==substrings[i]:
            pal.append(substrings[i])  
    
    long_palin=pal[0]            
    for i in range(1,len(pal)):
        if len(pal[i]) > len(long_palin):
            long_palin=pal[i]
    return long_palin  
              


ls="bab"
ls1=substring(ls) 
print(ls1)

