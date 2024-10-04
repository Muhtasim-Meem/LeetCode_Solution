def find_matching_index(s, t):
    index = []
    i = 0
    
    for j, char in enumerate(t):
        if i < len(s) and char == s[i]:
            index.append(j)
            i += 1
        if i == len(s):
            break

    return index==sorted(index)
# Example usage
s = 'abc'
t = 'ahcgdb'
matching_index = find_matching_index(s, t)
print(matching_index)
