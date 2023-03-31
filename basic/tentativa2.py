lista = []
while (True):
    a = int(input())
    if (a > 0):
        lista.append(a)
    else:
        break
if lista:
    i = 0
    x = 0 
    while (i < len(lista)):
        x = x + lista(i)
        i = i + 1
    x = x / len(lista)
    print (f'a media eh {x}')
else:
    print('Lista vazia')