import re
import os

def countsent(file):
    sent = 0
    s = open (file,'r')
    lines = s.readlines()
    for line in lines:
        if re.search('<se>',line):
            sent = sent + 1
        return sent

def file_countsent():
    cw = open ('countsent.txt','w',encoding='utf-8')
    for root, dirs, files in os.walk('news'):
        for f in files:
            cw.write(f+'\t'+str(countsent(os.path.join(root, f)))+'\n')

file_countsent()

#def table(files):
 #   with open ('table.csv', 'w', encoding = 'utf-8') as f:
  #      f.write('Название файла' + \t + 'Автор' + \t + 'Название текста' + \n)

