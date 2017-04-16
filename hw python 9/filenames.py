import os
import re
nonum = []
num = []
for f in os.listdir('.'):
    if re.search('[1234567890]', f):
        num.append(f)
    else:
        nonum.append(f)
print('Файлов, не содержащих цифр в названии: ', len(nonum))

    
