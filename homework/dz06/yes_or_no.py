def yes_or_no(s):
    n = 0
    q = []
    s1 = list(s)
    while len(s1) !=0:
        s2 = list(s)
        print(s1[0])
        q = s1[0]
        s1.remove(q)
        s2.remove(s[n])
        n += 1
        
        if q in s2:
            print('В списке присутствуют таки же элементы')
        else:
            print('Введенный элемент уникальный')
            
#s = input('Введите список: ')
s = (1,2,3,4,5,1,'q','w','q',1)
yes_or_no(s)