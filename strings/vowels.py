
def vowels_find(s:str):
    vowels="AEIOUaeiou"

    co=sum(1  for x in s if x in vowels )
    return co




print(vowels_find("basfhsflksia"))
