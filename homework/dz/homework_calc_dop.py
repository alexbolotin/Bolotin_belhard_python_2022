import decimal
from num2t4ru import decimal2text

int_units = ((u'.', u'.', u'.'), 'm')
exp_units = ((u'', u'', u''), 'f')
decimal2text(decimal.Decimal(),int_units=int_units,exp_units=exp_units)
s = []
ss = ['+', '-', '/', '**', '*']
n = 0

while s!='exit':
    s = input("Введите данные через пробел: ").split()
    try:
        if s[0] =='exit':   
            print('Спасибо, до скорых встреч!')
            break
        else:    
                if s[1] in ss:
                    x = float(s[0])
                    y = float(s[2])
                    n += 1 
                    if s[1] =='+':
                        print("Результат:\n",s[0],s[1],s[2],'=', (x+y),'\n', decimal2text( (x+y), places=1,int_units=int_units,exp_units=exp_units))
                        print('\nКоличество произведенных операций:', n)
                    elif s[1] =='-':
                        print("Результат:\n",s[0],s[1],s[2],'=', (x-y),'\n',decimal2text( (x-y), places=1,int_units=int_units,exp_units=exp_units))
                        print('\nКоличество произведенных операций:', n)
                    elif s[1] =='*':
                        print("Результат:\n",s[0],s[1],s[2],'=', (x*y),'\n',decimal2text( (x*y), places=1,int_units=int_units,exp_units=exp_units))
                        print('\nКоличество произведенных операций:', n)
                    elif s[1] =='/':
                        if y == 0:
                            print('\nДеление на 0 запрещено')
                        else:
                            print("Результат:\n",s[0],s[1],s[2],'=', (x/y),'\n',decimal2text( (x/y), places=1,int_units=int_units,exp_units=exp_units))
                            print('\nКоличество произведенных операций:', n)
                    elif s[1] =='**':
                        print("Результат:\n",s[0],s[1],s[2],'=', (x**y),'\n',decimal2text( (x**y), places=1,int_units=int_units,exp_units=exp_units))
                        print('\nКоличество произведенных операций:', n)
                else:
                        print('Введён неверный арифметический знак, введите согласно списку : +,-,*,/,**')
    except:
        print("Неверный ввод данных")

