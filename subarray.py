lst=[1,2,3,4,5,6,7,8,9]

def subarray(lst):
    sub=[]

    n= len(lst)

    for i in range(n):
        for j in range(i,n):
            sub.append(lst[i:j+1])
    return sub 

print(subarray(lst))       