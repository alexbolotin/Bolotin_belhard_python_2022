def char_counter(s):
    spisok = {}
    for i in s: 
        if i in spisok:
            spisok[i] += 1
        else:
            spisok[i] = 1
    # for i in spisok:
    #     print(f'"{i}" - "{spisok[i]}"')
    return spisok

STR_VAL = 'python is the fastest-growing major programming language'
# char_counter(STR_VAL)
print(char_counter(STR_VAL))

