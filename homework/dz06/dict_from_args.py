def sum_of_args(s):
    s1 = 0
    for i in s.split(','):
        s1 +=int(i)
    return s1

def kwargs_max_len(i):
    global max_len
    i_len = 0
    if type(i) == str:
            i_len = len(i)
            if max_len < i_len:
                max_len = i_len
    return max_len      

max_len = 0
sum = 0
s = '1,2,3,400,10'
#s = '1,2,3',[1,2,3],(1,2,3)
#s = '1,2,3,qwe'
#s = input('Введите список: ')

try:
    for i in s.split(','): 
        kwargs_max_len(i)
    print('kwargs_max_len = ', max_len)
    if all(i.isdigit() for i in s.split(',')):
        print('Сумма = ', sum_of_args(s))
    else:
        print('Все аргументы - ключевые слова должны быть строками')
    
except:
    print('Все аргументы - ключевые слова должны быть строками')