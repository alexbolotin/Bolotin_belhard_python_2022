def fibbonachi(n):
        a,b = 0, 1
        for i in range(1,n+1):
                sum = a + b
                a = b
                b = sum     
                yield sum

n = 0
while n != 'exit':
    n = input('Введите первоначальное число: ')
    if n == 'exit':
            break  
    elif n == '0':
            print('Введите число, отличное от 0')
    elif n == '1':
            print('0,1')
    elif n.isdigit() == False:
            print('Введите целое число')
    elif n.isdigit() == True:
            s = fibbonachi(int(n))
            print(list(s))


