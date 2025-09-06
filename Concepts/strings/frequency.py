str_dummy="i love python language"

freq={}

for ch in str_dummy:
    if ch in freq:
        freq[ch]+= 1
    else:
        freq[ch]=1
print(freq) 

