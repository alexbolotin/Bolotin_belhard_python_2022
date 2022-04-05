def decorator(funct):
    def wrapper(*args,**kwargs):
        print(f'Выполняем функцию {dop}{name}')
        funct(name,dop)
        print(f'Выполнено {dop}{name}')
    return wrapper

@decorator
def hello(name,dop):
    print(f'Привет {name}')



name = 'Alex'
dop ='decor.'
#name = input('Введите своё имя: ')

hello(name,dop)




