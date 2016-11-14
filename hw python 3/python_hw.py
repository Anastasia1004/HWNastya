a = []
s = str(input("Введите слово "))
while s != (""):
    if len(s) > 5:
        a.append(s)
    s = str(input("Введите слово "))
print('\n'.join(a))
    
