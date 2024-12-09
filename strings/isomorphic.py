def isomorphic_string(s: str, t: str) -> bool:
    
    s_mapping = {}
    t_mapping = {}

   
    if len(s) != len(t):
        return False

  
    for char_s, char_t in zip(s, t):
      
        if char_s in s_mapping:
            if s_mapping[char_s] != char_t:
                return False 
        else:
            s_mapping[char_s] = char_t  

       
        if char_t in t_mapping:
            if t_mapping[char_t] != char_s:
                return False 
        else:
            t_mapping[char_t] = char_s  
    return True 


# Test the function
if isomorphic_string("acc", "xzz"):
    print("True")
else:
    print("False")
