s="A man, a plan, a canal: Panama"
test_str = s.lower()
test_str = ''.join(letter for letter in test_str  if letter.isalnum())
print(test_str)
reversed_s = test_str[::-1]

if test_str == reversed_s:
    print("True")
else:
    print("False")