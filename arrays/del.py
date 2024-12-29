from array import *

arr=array('i',[90,45,1,2,3,4,5,6,7])
print(arr)

del_pos=3

for i in range(del_pos-1,len(arr)-1,1):
   
   arr[i]=arr[i+1]
arr.pop()  
print(arr) 

   