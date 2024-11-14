s="ab-cd"
lst=[i for i in s if i.isalpha()]
lst.reverse()
for i in range(len(s)):
    if not s[i].isalpha():
        lst.insert(i,s[i])
result = ''.join(lst)

print(result)        
