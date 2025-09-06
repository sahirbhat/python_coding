list_values=[2,3,5,3,4,2,2,2,3,5,3,3,3,3,3]
str_list= str( list_values)
print(str_list)
output = {}
max_key, max_value = 0,0
 
for i in str_list.split(","):
    
    if i  not in output:

        n=(str_list.count(i))
        if n > max_value:
            max_value=n
            max_key=i
output[max_key] =max_value 
print(output)          


  
#     if n > max_value:
#         max_value=n
#         max_key=i
print(max_key,max_value)   