height = int(input('Высота Ёлки: '))
simbol = input('Символ: ')
for i in range(height):
    if len(simbol) == 1:
       print(f"{' ' * (height - i)}{simbol * i}||{simbol * i}")
    else:
        print(f"{' ' * (height - i)*len(simbol)}{simbol * i}||{simbol * i}")
print(' ' * height * len(simbol) + '||')
