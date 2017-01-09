#четырёхстопный хорей
#будет без заглавных, потому что современная поэзия.
import random

def adj():
    a=[]
    with open ('adj.txt','r',encoding='utf-8') as f:
        a=f.read()
    return random.choice(a.split())

#одушевленные
def Petya():
    b=[]
    with open ('nouns_like_Petya.txt','r',encoding='utf-8') as f:
        b=f.read()
    return random.choice(b.split())

#неодушевленные
def kustik():
    k=[]
    with open ('nouns_like_kustik.txt','r',encoding='utf-8') as f:
        k=f.read()
    return random.choice(k.split())

def prep():
    c=[]
    with open ('prep.txt','r',encoding='utf-8') as f:
        c=f.read()
    return random.choice(c.split())

def adjfem():
    d=[]
    with open ('adjfem.txt','r',encoding='utf-8') as f:
        d=f.read()
    return random.choice(d.split())

def nounfem():
    e=[]
    with open ('nounfem.txt','r',encoding='utf-8') as f:
        e=f.read()
    return random.choice(e.split())

def verb():
    g=[]
    with open ('verbpf.txt','r',encoding='utf-8') as f:
        g=f.read()
    return random.choice(g.split())

def punct():
    h=[]
    with open ('punct.txt','r',encoding='utf-8') as f:
        h=f.read()
    return random.choice(h.split())

def verse1():
    return adj() + ' ' + Petya() + ' ' + verb() + ' ' + kustik() + punct()

def verse2():
    return prep() + ' ' + adjfem() + ' ' + nounfem() + punct()

def verse3():
    return adj() + ' ' + kustik() + ' ' + verb() + ' ' + Petya() + punct()

def verse4():
    return Petya() + ' ' + verb() + ' ' + nounfem() + punct()

def make_verse():
    verse = random.choice([1,2,3,4])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    elif verse == 3:
        return verse3()
    else:
        return verse4()

for n in range(4):
    print(make_verse())

