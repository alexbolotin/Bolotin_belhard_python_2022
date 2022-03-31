import decimal
from num2t4ru import decimal2text

int_units = ((u'.', u'.', u'.'), 'm')
exp_units = ((u'', u'', u''), 'f')
decimal2text(decimal.Decimal(),int_units=int_units,exp_units=exp_units)

s = ''
ss = ['+', '-', '/', '**', '*']
n = 0

while s!='exit':
    s = input("Введите знак (+,-,*,/,**): ")
    if s =='exit':
        print('Спасибо, до скорых встреч!')
    else:    
        if s in ss:
            x = float(input("x="))
            y = float(input("y="))
            n += 1 
            if s =='+':
                print("Результат:",decimal2text( (x+y), places=1,int_units=int_units,exp_units=exp_units), '\nКоличество произведенных операций:', n)
            elif s =='-':
                print("Результат:",decimal2text( (x-y), places=1,int_units=int_units,exp_units=exp_units), '\nКоличество произведенных операций:', n)
            elif s =='*':
                print("Результат:",decimal2text( (x*y), places=2,int_units=int_units,exp_units=exp_units), '\nКоличество произведенных операций:', n)
            elif s =='/':
                if y == 0:
                    print('Деление на 0 запрещено')
                else:
                   print("Результат:",decimal2text( (x/y), places=2,int_units=int_units,exp_units=exp_units), '\nКоличество произведенных операций:', n)
            elif s =='**':
                print("Результат:",decimal2text( (x**y), places=2,int_units=int_units,exp_units=exp_units), '\nКоличество произведенных операций:', n)
        else:
            print('Введён неверный арифметический знак, введите согласно списку : +,-,*,/,**')

