l1=[9,9,9,9,9,9,9]
l2=[9,9,9,9]
l1.reverse()
l2.reverse()
string1 = ''.join(map(str, l1))
string2 = ''.join(map(str, l2))
sum_result = int(string1) + int(string2)
x=str(sum_result)
lst = [int(char) for char in x]
lst.reverse()
print(sum_result)
print(lst)

    