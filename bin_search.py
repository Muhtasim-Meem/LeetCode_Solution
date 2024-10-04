def bin(lst,l,h,n):

    if l <= h:
        mid = (l+h) // 2

        if lst[mid]==n:
            return mid
        elif lst[mid] < n:
            return bin(lst,mid+1,h,n)
        else:
            return bin(lst,l,mid-1,n)
    return -1


lst=[1,2,3,5,7,9]
l=0
n=len(lst)

result=bin(lst,l,n-1,9)

if result==-1:
    print("Element not found")  
else:
    print(f"Element found at index {result}")
