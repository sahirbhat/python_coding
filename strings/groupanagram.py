from collections import defaultdict

def group_anagrams(s: list[str]):
    anagram = defaultdict(list)
    for word in s:
        # Sort the word to use it as a key
        sorted_word = ''.join(sorted(word))
        # Group anagrams by their sorted version
        anagram[sorted_word].append(word)
    
    # Return the dictionary where keys are sorted words
    return dict(anagram)

# Test the function
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)




def group_anagrams(s: list[str]):
    anagram = {}
    for word in s:
        # Sort the word to use it as a key
        sorted_word = ''.join(sorted(word))
        
        # If the sorted word is not already in the dictionary, initialize an empty list
        if sorted_word not in anagram:
            anagram[sorted_word] = []
        
        # Append the word to the corresponding anagram group
        anagram[sorted_word].append(word)
    
    return anagram

# Test the function
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
