#string frequency


str="hello world in world of python"

list_str=list(str)

freq=[ list_str.count(e) for  e in list_str]
print(freq)
d=dict(zip(list_str,freq))
print(d)

dict1={}
for s in str.split(" "):
    if s in dict1:
        dict1[s]+=1
    else:
        dict1[s]=1
print(dict1) 




