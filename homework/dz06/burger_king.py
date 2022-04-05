def bread(funct):
    def wrapper(*args,**kwargs):
        print('   ____________\n','</------------\\>')
        funct(meat)
        print(' <\\____________/>')
    return wrapper

def salad(funct):
    def wrapper(*args,**kwargs):
        print(' ~~~~ салат ~~~~~')
        funct(meat)
    return wrapper

def tomato(funct):
    def wrapper(*args,**kwargs):
        print(' *** помидоры ****')
        funct(meat)
    return wrapper

def cheese(funct):
    def wrapper(*args,**kwargs):
        print(' ^^^^^ сыр ^^^^^^')
        funct(meat)
    return wrapper

def onion(funct):
    def wrapper(*args,**kwargs):
        print(' ----- лук ------')
        funct(meat)
    return wrapper

@bread
@cheese
@salad
def test1(meat):
    print(' |||| курица ||||')

@bread
@onion
@tomato
def test2(meat):
    print(' ### говядина ###')

chiken = 1
beef = 2
meat=''
while meat != 'stop':
    try:
        meat = input(f'Сделайте выбор:\n 1 - курица\n 2 - говядина\n stop - для выхода из меню\n')
        if int(meat) == chiken:
            test1(meat)
        elif int(meat) == beef:
            test2(meat)
    except:
        print('выберете меню из предложенных позиций')
