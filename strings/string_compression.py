def string_compression(s:str):
    count=1
    str_comp=[]

    for i in range(1,len(s)):
        if s[i] ==s[i-1]:
            count+=1
        else:
            str_comp.append(s[-i]+ str(count))  
            count=1
    str_comp.append(s[-1]+str(count))    
    return  ''.join(str_comp)     



print(string_compression("aaabbbaabb"))