def decimal_to_base(n):
    if n < 2:
        return False
    
    results = []
    for base in range(2, n-1):
        digits = []
        number = n
        while number:
            digits.append(int(number % base))
            number //= base
        results.append(''.join(map(str, digits[::-1])))
        
    reversed_list = [element[::-1] for element in results]
    
    
    for i in range(len(reversed_list)):
        for j in range(len(reversed_list)):
            if reversed_list[i] != reversed_list:
                return False
            else:
                return True
    
    
    
                    
    
    


num = 4


base_conversions = decimal_to_base(num)
print(base_conversions)




