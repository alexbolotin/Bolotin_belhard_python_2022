def num_sum(q):
    s1 = 0
    sum = 0
    s = int(q)
    s_len = len((q))
    for i in range(s_len,-1,-1):
        s1 = s//10**i
        s -= s1*(10**i)
        sum += s1
    print(sum)


q = input('Введите любое число: ')
num_sum(q)
  

    

