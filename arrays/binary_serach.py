from array import *
def binary_serach(arr,ele):
    
    low=0
    high=len(arr)-1
   

    while low < high:
        mid=low+high//2
        if arr[mid]==ele:
            return mid
            
        elif arr[mid]> ele:
            high=mid-1
        else:
           low= mid+1  
    return -1        

    
    



arr=array("i",[34,56,78,90,100,109])
ele=90
result=binary_serach(arr,ele)
if result!=-1:
    print( "found")
else:
    print("not found")    