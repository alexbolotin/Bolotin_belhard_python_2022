def fibbonachi(m):
    fib = 0
    fib_old = 0
    fib_now = 1
    for i in range(1,m):
        fib = fib_old + fib_now 
        fib_old = fib_now
        fib_now= fib
        print(f'Fibbonachi ({m}), znachenie №({i}):',fib)

n = 0
while n != 'exit':
    n = input('Введите первоначальное число: ')
    if n == 'exit':
            break  
    elif n == '0':
            print('Введите число, отличное от 0')
    elif n == '1':
            print('1')
    elif n.isdigit() == False:
            print('Введите целое число')
    elif n.isdigit() == True:
            m = int(n)
            fibbonachi(m)
    
        
        
    



