s= "IIIV"
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
val = []

for i in range(len(s)):
    val.append(roman[s[i]])
print(val)    
total = 0

for i in range (len(val)-1):
    current = val[i]
    if current < val[i+1]:
        total -= current 
    else:
        total += current

total+= val[-1]

print(total)        

