import re
def vikings():
    wikifile = input('Время альтернативной истории! Введите имя файла со статьей про викингов: ')
    with open(wikifile, 'r', encoding = 'utf-8') as f:
        wikiarticle = f.read()
    return wikiarticle


def change1(wikiarticle):
    myarticle1 = re.sub('викинг', 'бурундук', wikiarticle)
    return myarticle1

def change2(myarticle1):
    myarticle2 = re.sub('Викинг', 'Бурундук', myarticle1)
    return myarticle2

def chimpunks(myarticle2):
    newfile = input('Введите имя файла, куда следует поместить измененную статью: ')
    with open(newfile, 'w', encoding = 'utf-8') as f:
              f.write(myarticle2)

def go():
    chimpunks(change2(change1(vikings())))

go()  
