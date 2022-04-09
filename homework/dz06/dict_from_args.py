def sum_of_args(args):
    sum = 0
    for i in args:
        sum +=int(i)
    return sum

def kwargs_max_len(kwargs):
        max_len = 0
        i_len = 0
        for i in kwargs:
                i_len = len(i)
                if max_len < i_len:
                        max_len = i_len
        return max_len      


def dict_from_args(*args, **kwargs):
        result = {}
        if all(type(i) is int for i in args):
                # print('Сумма = ', sum_of_args(args))
                result['sum_of_args'] = sum_of_args(args)       
        else:
                print('Все аргументы - должны быть целоочисленными')

        if all([type(i) is str for i in kwargs.values()]):
                # print('Максимальная длинна = ',kwargs_max_len(kwargs.values()))
                result['kwargs_max_len'] = kwargs_max_len(kwargs.values())
        else:
                print('Все аргументы - ключевые слова должны быть строками')
        return result


print(dict_from_args(1,2,3,4,5,q = '12',w = '12345',e = 'qwe',r = '1234'))