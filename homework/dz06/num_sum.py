def num_sum(s,n,sum):
    if n != 0:
        sum += int(s[n-1])
        n -= 1
        num_sum(s,n,sum)
    else: 
        print(sum)
 
# q = (input('Введите любое число: '))
q = '123451011110'
s = [i for i in q]
sum = 0
print(f'Сумма числа {q} :')
num_sum(s,len(q),sum)
