from collections import Counter


def single_number(lst):
    lst1=[]
    
    count=Counter(lst)
    
    for i in range(len(lst)):
        if lst.count < 2:
            lst1.append(lst[i]) 
    return lst1


lst=[1,1,1,2,2,2,3,3,3,4]  
res=(single_number(lst)) 
print(lst)       
    