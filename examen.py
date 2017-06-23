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

def text_data(txt1):
    topic = re.search(r'<meta content="(.*)" name="topic">', txt1).group(1)
    author = re.search(r'<meta content="(.*)" name="author">', txt1).group(1)
    data = [author, topic]
    return data

def csv(data, name):
    with open(name, 'a', encoding='cp1251') as f:
        f.write(data[2]+'\t'+data[0]+'\t'+data[1]+'\n')

def supertable():
    data1 = []
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='cp1251') as m:
                txt = m.read()
            data = text_data(txt)
            data.append(f)
            data1.append(data)
    for data in data1:
        csv(data, 'supertable.csv')

file_countsent()
       
supertable()
