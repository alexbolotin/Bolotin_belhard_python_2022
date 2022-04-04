def povtor(q,s1):
    b = 0
    for i in s1:
        if q == i:
            b +=1
    return b

def del_s1(s1):
    for i in s1:
        q = i
        w = povtor(q,s1)
        for i in range(w):
            s1.remove(q)
        print(f'Количество элементов {q} - {w}')


STR_VAL = 'python is the fastest-growing major programming language'

s1 = list(STR_VAL)
for i in s1:   
    if i == ' ' or i=='-':
        s1.remove(i)

w = 0
s1.sort()
s_len = len(s1)

for i in s1:
    del_s1(s1)
    




