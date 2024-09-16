#lst=[1,2,3,4,5,6,7]
#j=3

#for i in range(j):
#    x=lst.pop()
#    print(x)
#    lst.insert(0,x)
    #print(lst)
    
# TLE for test case 37/78


lst=[1,2,3,4,5,6,7]

k=3
x=len(lst)-k
y=k%x
print(y)

print(lst[-k:]+lst[:-k])       