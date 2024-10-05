def is_palindrome(s:str):
    return s ==s[::-1]







if is_palindrome("madam"):
    print("palindrome")
else:
    print("Not plaindrome")  

#method 2
def is_planidrome_rev(s:str) :
    rev=""

    for  char in s:
        rev= char + rev
    if rev==s:
        print(rev)
        return True
    else:
        print(rev)
        False    




if is_planidrome_rev("python"):
    print("palindrome")
else:
    print("Not plaindrome") 
       