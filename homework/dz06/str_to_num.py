def str_to_num(str):
    str = str.strip()
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():
        return int(str)

str_list = input('Введите список: ')
num_list = []
for i in str_list:
   n = str_to_num(i)
   if n is not None:
       num_list.append(n)

print(num_list)

