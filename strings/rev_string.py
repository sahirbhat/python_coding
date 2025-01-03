# Input : Hi i am raghu
 
# Output : uh g ar maiiH


def string_rev(s:str):
    new_str=""
    for i in s:
        new_str=i+new_str
    print(new_str)    

        





string_rev("Hi i am Raghu")
hell="hello i , m wonder"
rev_string=""
rev_string=hell[::-1]
print(rev_string)

for i in hell[::-1]:
    print(i, end="")
    