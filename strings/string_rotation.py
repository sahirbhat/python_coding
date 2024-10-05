def string_rotation_check(s: str, t: str) -> bool:
    # Step 1: Check if lengths are the same
    if len(s) != len(t):
        return False  # Return False if lengths are different

    # Step 2: Check if t is a substring of s concatenated with itself
    return t in (s + s)

# Example usage
if(string_rotation_check(s="waterbottle", t="watermelon")):
    print("Rotated")
else:
    print("Not ")      # Output: True
