def find_position(lst,target):
    lst1 =[]   
             
    for i in range(len(lst)):
        if lst[i]==target:
            lst1.append(i)
    if len(lst1)==0:
        return [-1,-1]
    else:
        return [lst1[0],lst1[-1]]

    
    


lst=[5,7,7,10]  
x=8

print(find_position(lst,x))  # Output: [-1,-1]
    
            