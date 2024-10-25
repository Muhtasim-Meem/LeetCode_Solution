lst1=[-1,-1,-1,-1,-1,-1,-2,-2]
for i in range(len(lst1) - 1, -1, -1):
    x = lst1.count(lst1[i])
    if x > 2:
        lst1.pop(i)

print(lst1)        