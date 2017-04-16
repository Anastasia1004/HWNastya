with open('ugadaika.csv', 'r', encoding = 'utf-8') as f:
    words = []
    a = f.read()
    words = a.split(',')
    dic = {}
    for i, word in enumerate(words):
        if i%2 == 0:
            dic[word] = words[i+1]
    print('Я хочу сыграть с тобой в одну игру... Какое слово я загадал? Количество точек равно количеству букв в слове.')
    for key in dic:
        print(dic[key])
        b = input()
        if b == key:
            print('Молодчинка!!!')
        else:
            print ('Ты не очень умный, я загадал не это.')

