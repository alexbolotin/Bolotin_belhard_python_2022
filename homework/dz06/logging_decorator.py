def decorator(funct,*args,**kwargs):
    def wrapper(*args,**kwargs):
        print(f'Выполняем функцию {funct.__name__} с args {args} и kwargs {kwargs}')
        funct(name)
        print(f'Выполнено {funct.__name__}')
    return wrapper

@decorator
def hello1(name,*args,**kwargs):
    print(f'Привет {name}')


name = 'Alex'
age = 12
#name = input('Введите своё имя: ')

hello1(name,age,n = 1,q = 2)




