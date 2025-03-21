lst=[1,2,5,6,"Muhtasim",9.0,'a']
print(lst[1::])

from collections import Counter

count = Counter(lst)
print(count)    

x=5
y=10
while x!=0:
    print(y)
    x-=1

dict ={
    "name":"Muhtasim",
    "age":24,
    "address":"Dhaka",
    "phone":1234567890
}

print(dict["name"])
print(type(dict.get(("name"))))