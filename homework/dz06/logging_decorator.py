def hello(name):
    def decor():
        x = 'decor.'
        print(f'Выполняем функцию {x}.{name}')
        print(f'Привет {name}')
        print(f'Выполнено {x}.{name}')
    return decor


b = 'Alex'
#n = input('Введите своё имя: ')

a = hello(b)
a()



