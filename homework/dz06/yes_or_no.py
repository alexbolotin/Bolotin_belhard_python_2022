def yes_or_no(s):
    spisok = {}
    for i in s: 
        if i in spisok:
            spisok[i] += 1
            print(f'Элемент {i} Yes')
        else:
            spisok[i] = 1
            print(f'Элемент {i} No')


#s = input('Введите список: ')
s = (1,10,2,3,'q',4,5,1,'q','w','q',1,'q',1,1,'q',1,1,'q',1,1)
yes_or_no(s)

