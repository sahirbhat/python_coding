from array import *

arr=array("i",[89,56,33,44,55,66,77,33,6,23])

max1=0
max2=0



for i in arr:
    if i > max1:
        max2=max1
        max1=i
    elif max2 <  i and i!=max1:
        max2=i
print(f"highest two ele of an raay is {max1} and {max2}")        
