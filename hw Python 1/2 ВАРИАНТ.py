print('Введите число a и нажмите Enter')
a=int(input())
print('Введите число b и нажмите Enter')
b=int(input())
print('Введите число c и нажмите Enter')
c=int(input())
if a*b==c:
    print(c ,'является произведением', a,' и ', b)
else:
     print(c ,' не является произведением', a,' и ', b)
if c*a==(-1)*b:
    print(c,'является решением линейного уравнения', a,'x +',b,'= 0')
else:
     print(c,'не является решением линейного уравнения', a,'x +',b,'= 0')
