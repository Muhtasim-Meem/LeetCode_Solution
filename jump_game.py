lst=[1,4,4,2,2,13,5,5,1]
lst.sort()

i=0

while i < len(lst)-1:
    if lst[i] ^ lst[i+1]==0:
        lst.pop(i)
        lst.pop(i)
    else:
        i+=1
print(lst)        
        
    