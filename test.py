import re
def openfile():
    file1 = input('Введите путь к файлу: ')
    with open(file1, "r", encoding="utf-8") as f:
        arr = []
        lines = f.readlines()
        for line in lines:
            if line.strip() == '<text>': #строка, которая идет после </teiHeader>
                break
            else: arr.append(line)
        print('Число строк заголовка', len(arr)) #task 1 done
    
def dictionary():
    file2 = input('Введите путь к файлу: ')
    with open(file2, "r", encoding="utf-8") as f:
        dictn = {}
        text = f.read()
        findtype = re.findall(r'type="\w+">', text)
        for i in findtype:
            i = i[6::].strip('">')
            if i not in dictn:
                dictn[i] = 1
            else:
                dictn[i] += 1
    file3 = input('Введите путь к файлу, куда будет записана информация из словаря: ')
    with open(file3, "r", encoding="utf-8") as f:
        for key in dictn:
            f.write(str(key, dictn[key])) #ну почти
            
openfile()   
dictionary()
       
    
    
    
    
        
