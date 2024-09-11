lst=[[1,3]]

def merge_intervals(lst):
    lst.sort()
    i=0
    while i < len(lst)-1:
        if lst[i][1]>=lst[i+1][0]:
            lst[i][1]=max(lst[i][1],lst[i+1][1])
            lst.pop(i+1)
        else:
            i+=1
    return lst

print(merge_intervals(lst)) # Output: [[1, 6], [8, 10], [15, 18]]