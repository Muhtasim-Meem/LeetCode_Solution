nums=[555,901,482,1771]
count = 0

for x in nums:
    y=str(x)
    z=len(y)
    if z%2==0:
        count+=1
print(count)    