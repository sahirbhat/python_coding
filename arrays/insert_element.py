from array import *

arr=array('i',[8,5,3,2,9,66,55,12,45,6])

insert_element=420
inser_pos=3

arr.append(0)

for i in range(len(arr)-1,inser_pos-1,-1):

    arr[i]=arr[i-1]


arr[inser_pos]=insert_element
print(arr)    