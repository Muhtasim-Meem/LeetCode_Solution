res=[]
for i in range(47,85+1):
    y=i
    x=0
    while  i > 0:
        r=i%10
        if r == 0 or y%r !=0:
            x=1
            break
        i=i//10
    if x==0:
        res.append(y)        
       
print(res)        
    
    

x = 128
res = []

for i in range(47, 85 + 1):
    y = i  
    valid = True
    
    while i > 0:
        r = i % 10
        if r == 0 or y % r != 0:  
            valid = False
            break
        i = i // 10
    
    if valid:
        res.append(y)

print(res)