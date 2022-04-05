def rec(l,n):
    while len(l) != 0:
        
        if type(l[0]) == int:
            s = l[0]
            probel = ' '
            print(f'{probel*n}{s}')
            l.pop(0)
        
            
        elif type(l[0]) == list:
            n +=4
            l1 = l[0]
            l.pop(0)
            rec(l1,n)
            n = 0


l = [1,2,[3,4,[1,2,3]],5,6,7,[1,2,3,4]]
n = 0
print(l)
rec(l,n)



