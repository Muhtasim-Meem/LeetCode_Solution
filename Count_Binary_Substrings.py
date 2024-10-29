s="00110011"

res=[]

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
                if len(s[i:j])%2==0 and len((s[i:j]))>=2:
                    if s[i:j].count('0')==s[i:j].count('1'):
                        res.append(s[i:j])
print(res)                        

result =[]
for c in res:
    count0 = count1 = 0
    prv = c[0]
    valid = True

    for char in c:
        if char == '0':
            if prv == '1':
                count0 = 0
            count0 += 1
        else:
            if prv == '0':
                count1 = 0
            count1 += 1

        if count0 != count1:
            valid = False
            break

        prv = char

    if valid:
        result.append(c)
print (result)        