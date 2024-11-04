word="a3e"
n= len(word)
vowels=0
consonent = 0
digits = 0
test_str = ''.join(letter for letter in word if letter.isalnum())

if len(test_str) == n:
    for i in range(n):
        if word [i] in "aeiouAEIOU":
            vowels += 1
        if word[i] in "0123456789":
            digits += 1
    consonent = n - (vowels + digits)    
else:
    print("Invalid input")
    exit()     

if len(test_str) >=3 and consonent >=1 and vowels >=1:
    print("Valid")
else:
    print("Invalid")

