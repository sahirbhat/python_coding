string_Input= "mississippi" 
max_ch=0

for ch in string_Input:
    if ch.count(string_Input)> max_ch:
        max_ch=ch
print(ch)        



str_dummy="i love python"

for word in str_dummy.split()[::-1]:
    print(word,end=" ")

#anagram
str1="silent"
str2="listen" 

if len(str1)==len(str2):
    if sorted(str1)==sorted(str2):
        print('anagram')
    else:
        print("not anagram")    
else:
    print("not anagram")        

 #frequency
str_dummy="i love python language"

freq={}

for ch in str_dummy:
    if ch in freq:
        freq[ch]+= 1
    else:
        freq[ch]=1
print(freq) 


#duplicate remove
str_duplicate="programming"
without_duplicate=""
for ch in str_duplicate:
    if ch not in without_duplicate:
        without_duplicate+=ch
print(without_duplicate)        



string_ex="hello I love pythOn programminG"

vowel= sum(1  for ch in string_ex if ch.lower() in 'aeiou')
print(vowel)


s1="waterbolltle"
s2="watermelon"

if len(s1)==len(s2):
    if s1 in (s1+s2):
        print('yes')
else :
    print('not')  


str1 = "abc"
substrings = []
for i in range(len(str1)):
    for j in range(i+1, len(str1)+1):
        substrings.append(str1[i:j])

print(substrings)


