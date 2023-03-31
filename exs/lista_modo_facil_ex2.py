lista1 = set(input().split())
lista2 = set(input().split())
lista3 = []
print(lista1 & lista2)
for i in lista1:
    for a in lista2:
        if i == a:
            lista3.append(a)       
print(lista3)