words_list = ['apricot', 'apple', 'ant', 'banana', 'boy', 'balance', 'manago', 'man', 'cat']

freq_words = {}

# for word in words_list:
#     ch = word[0]
#     if ch in freq_words:
#         freq_words[ch].append(word)
#     else:
#         freq_words[ch] = [word]  # Initialize with a list

# print(freq_words)

for word in words_list:
    ch=word[0]
    if ch in freq_words:
        freq_words[ch].append(word)
    else:
        freq_words[ch]= [word ] 
print(freq_words)          


words_list = ['sun', 'apple', 'ant', 'banana', 'boy', 'balance', 'man', 'cat', 'elephant']
freq_words={}

for word in words_list:
    n=len(word)
    if n in freq_words:
        freq_words[n].append(word)
    else:
        freq_words[n]=[word]    
print(freq_words)  


words_list = ['apple', 'banana', 'cat']
f={}
for ch in "".join(words_list):
    vowels=sum(1 if ch in 'aeiou')
    if ch in f:
        f[ch]+=1
    else:
        f[ch]=1
print(f)            
    

