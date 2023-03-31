import random
print(max((6 + 3.5)/2,(6 + 2.5)/2,(3.5 + 2.5)/2,2.5))
print(random.randrange(2))#gera numeros entre 0 e 1
print(random.randint(1,2))#gera numeros entre 1 e 2
for i in range(5):#vai exibir os numeros de 0 a 4
    print(i)
for numero in range(10):
    if numero %2 == 0:
        print(numero)
lista = [1,4,9,16,25,36]
print(len(lista))#mostra o tamanho da lista
print(lista[0])#primeira variavel da lista
print(lista[-1])#ultima variavel da lista
print(lista[-3:])#retorna os 3 ultimos
print(lista[2:5])#começa na segunda variavel e termina na quinta
lista[0] = 82 #troca a primeira variavel para 82
lista.append #adiciona um item ao final da lista
while len(lista) > 0:
    print(lista)
    break

        