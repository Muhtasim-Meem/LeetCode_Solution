s= "FlaG"
valide = False
if  s.isupper():
    valide = True
elif s.islower():
    valide = True
elif s[0].isupper() and s[1:].islower():
    valide = True
else:
    valide = False         

print(valide)              