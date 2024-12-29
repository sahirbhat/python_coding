
from collections import ChainMap
def merge_dic(*dicts):
    d3 = {}
    for dic in dicts:
        d3.update(dic)
    print(d3)  # Print the merged dictionary


# Sample dictionaries
dict1 = {"apple": 1, "mango": 3}
dict2 = {"orange": 9, "banana": 8}
dict4={"grapes":90,"ppaya":76}

print("_____________________________________________")
print(dict4.get("grapes","not found"))

# # Direct merge using the | operator
# print(dict1 | dict2)  # Output: {'apple': 1, 'mango': 3, 'orange': 9, 'banana': 8}

# Merge using the custom function
merge_dic(dict1, dict2) 
print("2nd method")
dict1.update(dict2)
print(dict1)

merged_dictionary={}
print("third method")
merged_dictionary= {**dict1,**dict2}
print(merged_dictionary)

print("4th method")
print(dict(ChainMap(dict1,dict2)))

dict1["cherry"]=90
print("new value added")
print(dict1)

for k,v in dict1.items() :
    if k =='apple' :
        print(dict1)
        # del dict1[k] 
        # print("completede",dict1) 
