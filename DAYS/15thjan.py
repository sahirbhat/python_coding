from array import *

""" 
target sum of two elements 
"""

def target_sum(n):
    print(n)
    target=14
    high=len(n)-1
    low=0
    while low <high:
        current_sum=n[low]+n[high]
        if current_sum==target:
            print(f"found {low},{high} index {target}")
            break
        elif target >  current_sum:
            low+=1
        else:
            high-=1
    else:
        print("not found")        




lst=[1,3,4,6,8,12]
target_sum(lst)




"""
    container max water

"""

def max_water(n):
    low=0
    high=len(n)-1
    max_cap=0
    while low<high:
        width=high-low
        min_lth=min(n[low],n[high])
        vol=width*min_lth
        max_cap=max(vol,max_cap) 
        if n[low]<n[high]:
            low+=1
        else:
            high-=1        
    return max_cap      

lst=[7,2,5,6,8,9]
print(max_water(lst))   



"""
Dutch National Flag

"""
def dutch_national_flag(lst):
    n=len(lst)-1
    low=0
    mid=0
    high=len(lst)-1
    while mid <= high:
        if lst[mid]==0:
            lst[low],lst[mid]=lst[mid],lst[low]
            low+=1
            mid+=1
        elif lst[mid]==1:
            mid+=1
        else:
            lst[mid],lst[high]=lst[high],lst[mid] 
            high-=1
    return lst               



lst=[1,0,1,0,1,2,2,1,0,1,2,0]
print(len(lst))


z=dutch_national_flag(lst)
print(z)

"""
insertion of an element



"""

from array import *
arr=array("i",[1,3,5,6,1])
arr.append(0)

ele=999
pos=3
for i in range(len(arr)-1,pos-1,-1):
    arr[i]=arr[i-1]

arr[pos]=ele


print(arr)


