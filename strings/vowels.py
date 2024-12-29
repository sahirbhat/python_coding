
def vowels_find(s:str):
    vowels="AEIOUaeiou"

    co=sum(1  for x in s if x in vowels )
    return co




print(vowels_find("basfhsflksia"))



def vowels_count(s:str):

    vowels="AEIOUaeiou"
    count=0
    count=sum( 1 for ch in s if ch in vowels)
    return count




print(vowels_count("Abjkdshfkjdsklfkjdhwrwqrzxvxa"))

