def is_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    map_str1_to_str2 = {}
    map_str2_to_str1 = {}

    for char1, char2 in zip(str1, str2):
        if (char1 in map_str1_to_str2 and map_str1_to_str2[char1] != char2) or \
           (char2 in map_str2_to_str1 and map_str2_to_str1[char2] != char1):
            return False

        map_str1_to_str2[char1] = char2
        map_str2_to_str1[char2] = char1

    return True

# Test cases
print(is_isomorphic("egg", "add"))  # True