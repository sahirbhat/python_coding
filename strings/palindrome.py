# def is_palindrome(s:str):
#     return s ==s[::-1]







# if is_palindrome("madam"):
#     print("palindrome")
# else:
#     print("Not plaindrome")  

# #method 2
# def is_planidrome_rev(s:str) :
#     rev=""

#     for  char in s:
#         rev= char + rev
#     if rev==s:
#         print(rev)
#         return True
#     else:
#         print(rev)
#         False    




# if is_planidrome_rev("python"):
#     print("palindrome")
# else:
#     print("Not plaindrome") 





def valid_palindrome(s):
    # Filter only alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

str_s = "A man, a plan, a canal: Panama"

if valid_palindrome(str_s):
    print("Palindrome")
else:
    print("Not a palindrome")

       