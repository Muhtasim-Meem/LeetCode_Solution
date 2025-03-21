def single_element(lst):

    res = set(lst)

    if len(res) != len(lst):
        print("List has duplicate elements")
    else:
        print("List has no duplicate elements") 

lst = [1,2,3,4,5,6]
single_element(lst) # List has no duplicate elementsN        