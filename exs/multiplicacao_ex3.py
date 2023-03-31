lista = list(map(int,input("insira os numeros ").split()))
x = int(input("insira um numero "))
acho = True
for i in lista:
    for n in lista:
        if i != n and i * n == x:
            print( i,"*",n,"= x")
            achou = False
            break
if not achou :
    print("numeros indisponiveis")

