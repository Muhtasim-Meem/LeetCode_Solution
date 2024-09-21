lst=[3,5,1,2,5,7]

lst2=lst
lst2.sort()

count = 0
for x in lst:
    for j in lst2:
        if x != j:
            count += 1
print(count)            