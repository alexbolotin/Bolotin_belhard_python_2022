def yes_or_no(s):
    if len(set(s)) == len(s):
        print('Введенный список уникальный')
    else:
        print('В списке присутствуют одиниковые элементы')




s = input('Введите список: ')
yes_or_no(s)