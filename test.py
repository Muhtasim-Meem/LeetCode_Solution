s="abc"
t="ahbgdc"

index=[]

for i in range(len(t)):
    if s[i] == t[i]:
        index.append(i)
print(index)        