mylist = [] 
with open('proga.txt', 'r', encoding='utf-8') as f: 
    for line in f.readlines(): 
        x = len(line) 
        mylist.append(x) 
mini = mylist[0] 
maxi = mylist[0] 
for i in mylist: 
    if i <= mini: 
        mini = i 
    if i > maxi: 
        maxi = i 
print(maxi/mini)
    
