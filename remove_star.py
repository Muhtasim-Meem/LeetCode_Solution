s = "erase*****"
t=""

def removestar(lst):
    stack=[]
    for i in lst:
        if i=="*":
            if stack:
                stack.pop()
            else:
                pass 
        else:
            stack.append(i)
    return stack

res=removestar(s)   
print("".join(res))                
