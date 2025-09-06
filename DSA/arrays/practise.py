from array import *

arr=array("i",[90,34,56,78,1,2,4,34])

#insertionn of an element:

low=0
high=len(arr)-1
insert_ele=999
position=5
arr.append(0)

for i in range(len(arr)-1,position-1,-1):
    arr[i]=arr[i-1]

arr[position]=insert_ele
print(arr)  


#delete of an array element

position_del=4
for i in range(position,len(arr)-1):
    arr[i]=arr[i+1]
print(arr)


#target sum of two

arr=array("i",[66,77,12,45,1,2,3,4,5,6])
arr=sorted(arr)
target_sum=5
current_sum=0
low=0
high=len(arr)-1



while low < high:
    current_sum=arr[low] + arr[high]
    if current_sum==target_sum:
        print("found")
        break
    elif target_sum > current_sum:
            low += 1
    else:
         high -= 1  
else:
     print("not found")   



#practices for conatiner volume maximum

arr=array("i",[3,4,8,1,9,])
# arr=sorted(arr)

low=0
high=len(arr)-1
max_cont=0

while low < high:
     
    width=high-low
    lht=min(arr[low],arr[high])
    volume=width * lht
    max_cont = max(volume,max_cont)

    if arr[low] < arr[high]:
         low+=1
    else:
         high-=1
print(max_cont)  


#binary search

arr=array("i",[1,5,9,11,34,56,99])

low =0
high=len(arr)-1
search_ele=99

while low<=high:
     mid = (low +high)//2
     if arr[mid]== search_ele:
          print(f"found {mid}")
          break
     elif search_ele > mid:
          low+=1
     else:
          high-=1
else:
     print("not found")  


#prouct of an array except itself

arr=array("i",[1,2,5,6])
n=len(arr)
print(n)



result=[1]*n

product_left=1

product_right=1

for i  in range(n):
     result[i]=product_left
     product_left*=arr[i]

for i in range(n-1,-1,-1):
     result[i]*=product_right
     product_right*=arr[i]


print(result)






