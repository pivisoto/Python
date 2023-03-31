def lerlista(l,n):
    i = 0
    while i < n:
        x = float(input("digite o valor: "))
        l.append(x)
        i = i + 1
n_valores = int(input("digite a quantidade de valores desejados nessa conta: "))
lista = []
lerlista(lista,n_valores)
media = sum(lista)/len(lista)
print (media)
desvio = np.std(lista)
print(desvio)


