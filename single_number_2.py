from collections import Counter


lst=[1,1,1,2,3,3,3,4,4,4]

def remove_duplicates(lst):

    new_lst = []

    count=Counter(lst)
    
    for x in lst:
        if lst.count(x)==1:
            new_lst.append(x)       

    i=0
    for x in new_lst:
        i^=x
    return i

print(remove_duplicates(lst)) 




# alternative solution

""" def remove_duplicates_optimized(lst):

    count=Counter(lst)
    
    for x in lst:
        if count[x]==1:
            return x """
