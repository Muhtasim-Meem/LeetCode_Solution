lst=[1,1,2,3,3,4,4,5,5]

res=0
for x in lst:
    if lst.count(x)==1:
        res^=x
print(res)        