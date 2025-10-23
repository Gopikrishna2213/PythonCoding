size=input('enter the size of pizza ?\ns=small\nl=larger\nm=medium   :')
pepper=input('do you want add pepper? y 0r n   :')
p=0
chesse=input('do you want add extra chesse? y or n   :')
if size=='s':
    print('pizza prize is $12')
    p=p+12
    if pepper=='y' :
        print('pepper price is $1')
        p=p+1
    else :
        p=p+0
    if chesse=='y' :
        print('for extra chesse price is $1')
        p=p+1
    else :
        p=p+0
    print(f'total pizze price is ${p}')
if size=='l':
    print('pizza prize is $24')
    p=p+24
    if pepper=='y' :
        print('pepper price is $3')
        p=p+3
    else :
        p=p+0
    if chesse=='y' :
        print('for extra chesse price is $2')
        p=p+2
    else :
        p=p+0
    print(f'total pizze price is ${p}')
if size=='m':
    print('pizza prize is $18')
    p=p+18
    if pepper=='y' :
        print('pepper price is $3')
        p=p+3
    else :
        p=p+0
    if chesse=='y' :
        print('for extra chesse price is $2')
        p=p+2
    else :
        p=p+0
    print(f'total pizze price is ${p}')
