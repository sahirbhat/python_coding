



weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
# output: [[‘wed’, 1], [‘sun’, 2], [‘thu’, 1], [‘tue’, 1], [‘mon’, 3], [‘fri’, 1]]

d={}

for days in weekdays:
    if days in d:
        d[days]+=1
    else:
        d[days] =1
print(d)        
 
