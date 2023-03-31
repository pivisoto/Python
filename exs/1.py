a = list(map(int,input("Digite os valores com espaços entre eles: ").split(" ")))
x = int(input("para deixar os numeros em ordem crescente digite 1 e para deixar os numeros em ordem descrescente digite 2: "))
if x == 1 :
    a.sort()
    print(a)
elif x == 2:
    a.sort()
    a.reverse()
    print(a)
else:
    print("você digitou um número inválido")

    