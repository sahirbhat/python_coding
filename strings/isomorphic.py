def isomorphic_string(s: str, t: str) -> bool:
    s_mapping = {}
    t_mapping = {}

    # Check if lengths are different, return False if they are
    if len(s) != len(t):
        return False

    # Iterate through both strings at the same time
    for char_s, char_t in zip(s, t):
        # Check if there's already a mapping for char_s in s_mapping
        if char_s in s_mapping:
            if s_mapping[char_s] != char_t:
                return False  # Mismatch in expected mapping
        else:
            s_mapping[char_s] = char_t  # Create new mapping

        # Check if there's already a mapping for char_t in t_mapping
        if char_t in t_mapping:
            if t_mapping[char_t] != char_s:
                return False  # Mismatch in expected mapping
        else:
            t_mapping[char_t] = char_s  # Create new mapping

    return True  # If all checks pass, the strings are isomorphic


# Test the function
if isomorphic_string("acc", "xzz"):
    print("True")
else:
    print("False")
