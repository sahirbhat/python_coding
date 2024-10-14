def are_permutations(str1: str, str2: str) -> bool:
    # Step 1: Check if lengths are the same
    if len(str1) != len(str2):
        return False
    
    # Step 2: Initialize dictionaries for character frequencies
    freq1 = {}
    freq2 = {}
    
    # Count frequencies for str1
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
            
    # Count frequencies for str2
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
            
    # Step 3: Compare the frequency dictionaries
    return freq1 == freq2

# Example usage
string1 = "abc"
string2 = "cba"
result = are_permutations(string1, string2)
print(result)  # Output: True

string3 = "abc"
string4 = "def"
result = are_permutations(string3, string4)
print(result)  # Output: False



# for char in str1:
#         freq1[char] = freq1.get(char, 0) + 1  # Count characters in str1
    
#     for char in str2:
#         freq2[char] = freq2.get(char, 0) + 1  # Count characters in str2

    # return freq1 == freq2  # Compare the two frequency dictionaries