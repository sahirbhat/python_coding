def balanced_string(s:str)->bool:
    stack=[]
    pair={'}':'{',']':'[',')':'('}
    for ch in s:
        if ch in pair.values():
            stack.append(ch)
        elif ch in pair.keys():
            # If the stack is empty or the top of the stack doesn't match, it's not balanced
            if not stack or stack.pop() != pair[ch]:
                return False

    # If the stack is empty at the end, the string is balanced
    return True



if balanced_string("({[]]})"):
    print("balanced")
else:
    print("not balanced")    


string = "Hello, world!"
substring = "world"

index = string.find(substring)
print(index)

if index != -1:
    print(f"The substring '{substring}' is found at index: {index}")
else:
    print(f"The substring '{substring}' is not found.")
