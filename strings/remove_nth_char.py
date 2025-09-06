string="python"
n=2
print(string[0:n]+string[n+1:])

print(string[-1]+string[1:len(string)-1]+string[0])


for char in string[0::2]:
    print(char,end="")

# find each word occurences    



for word in string[::-1]:
    print(word, end="")
    
