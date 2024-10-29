def maximumsub(lst):
    max_sum=lst[0]
    ar=[]

    for i in range(len(lst)):
        current_sum=0
        for j in range(i,len(lst)):
            current_sum+=lst[j]
            if current_sum>max_sum:
                max_sum=current_sum
                ar=(lst[i:j+1])
    return max_sum,ar

arr = [2, 3, -8, 7, -1, 2, 3]
print(maximumsub(arr))            
