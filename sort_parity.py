lst=[2,3,4,5]
lst2=[]
lst3=[]
for i in range(len(lst)):
    if lst[i]%2!=0:
        y=i
        lst2.append(y)
for x in lst:
    if x%2!=0:
        lst3.append(x)        
print(lst3)

lst2.sort(reverse=True)
print(f"Okay {lst2}")
for x in lst2:
    if 0 <= x < len(lst):
        del lst[x]  
for x in lst3:
    lst.append(x)
print(lst)            
        