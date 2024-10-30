n = 14

def  ugly(n):
    if n <=0:
        return False
    
    fact = [2,3,5]

    for i in fact:
        while n % i == 0:
            n = n/i
    return n == 1

print(ugly(n))        