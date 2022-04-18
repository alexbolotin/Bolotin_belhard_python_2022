import re

def counter(s):
    spisok = {}
    for i in s: 
        if i in spisok:
            spisok[i] += 1
        else:
            spisok[i] = 1
    return spisok

def sorted_dict(val):
    sorted_dict = {}
    sorted_keys = sorted(val, key=val.get, reverse= True)
    for i in sorted_keys:
        sorted_dict[i] = val[i]
    return sorted_dict

def finall(val):
    n = 0
    final_dict = {}
    for i in val:
        if n == 3:
            break
        else:
            final_dict[i] = val[i]
            n += 1
    return final_dict

s = '''Существует культ Питона, называемый "Дзеном Питона" (The Zen of Python).
Автором этих постулатов считается Тим Пейтерс.
Основные постулаты:
Красивое лучше, чем уродливое.
Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложное лучше, чем запутанное.
Плоское лучше, чем вложенное.
Разреженное лучше, чем плотное.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибки никогда не должны замалчиваться.
Если не замалчиваются явно.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один — и, желательно, только один — очевидный способ сделать это.
Хотя он поначалу может быть и не очевиден, если вы не голландец. [1]
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить — идея плоха.
Если реализацию легко объяснить — идея, возможно, хороша.
Пространства имён — отличная штука! Будем делать их побольше.'''

dict1 = re.sub(r'[^\w\s]','', s)
dict1 = counter(s.lower().split())

dict_sorted = sorted_dict(dict1)

final_dict = finall(dict_sorted)

print(final_dict)