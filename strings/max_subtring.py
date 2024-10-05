def length_of_longest_substring(s: str) -> int:
    char_set = set()  # To keep track of characters in the current window
    start = 0         # Pointer to the start of the current window
    max_len = 0       # The maximum length of substring found so far
    
    for end in range(len(s)):  # Move the `end` pointer from left to right
        # If we encounter a repeating character, shrink the window from the left
        while s[end] in char_set:
            char_set.remove(s[start])  # Remove the character at `start` from the set
            start += 1                 # Move the start pointer to the right
        
        char_set.add(s[end])  # Add the current character to the set
        max_len = max(max_len, end - start + 1)  # Update the max length if needed
    
    return max_len  # Return the maximum length found
print(length_of_longest_substring("abc"))





