dummy_dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key,value in dummy_dict1.items():
    print(key, value)

dummy_dict1["pin"]=19005
print(dummy_dict1)

dummy_dict1["name"]="Sahir_bhat"
print(dummy_dict1)
del dummy_dict1["age"]
print(dummy_dict1)

for key in dummy_dict1.keys():
    if "name" ==key:
        print("print found")



list1=[1, 2, 2, 3, 3, 3]
freq={}
for element in list1:
    if element in freq:
        freq[element]+=1
    else:
        freq[element]  =1
print(freq)          

dictionary = {"a": 10, "b": 20, "c": 5}

max_value = float('-inf')  # Smallest possible value
min_value = float('inf')   # Largest possible value

for value in dictionary.values():
    if max_value < value:
        max_value = value
    if min_value > value:
        min_value = value

print(max_value, min_value)
dictionary = {"a": 10, "b": 20, "c": 5}

max_value = max(dictionary.values())
min_value = min(dictionary.values())

print(max_value, min_value)

swap={"x": 1, "y": 2}
new_swap={}
for k,v in swap.items():
    new_swap[v]=k
print(new_swap) 

# Group by Key: Given a list of dictionaries, group them by a specific key. Input: [{"key": "a", "value": 10}, {"key": "b", "value": 20}, {"key": "a", "value": 15}]
# Output: {"a": [10, 15], "b": [20]}

    
                   