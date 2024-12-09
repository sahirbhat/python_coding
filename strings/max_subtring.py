def length_of_longest_substring(s: str) -> int:
    char_set = set()  
    start = 0         
    max_len = 0      
    for end in range(len(s)):  
        while s[end] in char_set:
            char_set.remove(s[start])  # Remove the character at `start` from the set
            start += 1               
        
        char_set.add(s[end])  # Add the current character to the set
        max_len = max(max_len, end - start + 1)  # Update the max length if needed
    
    return max_len  # Return the maximum length found
print(length_of_longest_substring("abccdedfc"))





