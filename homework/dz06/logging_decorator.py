def decorator(funct):
    def wrapper(*args,**kwargs):
        print(f'Выполняем функцию {funct.__name__}')
        funct(name)
        print(f'Выполнено {funct.__name__}')
    return wrapper

@decorator
def hello1(name):
    print(f'Привет {name}')


name = 'Alex'
#name = input('Введите своё имя: ')

hello1(name)




