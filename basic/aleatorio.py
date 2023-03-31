from random import randint

a = int(input( "Digite o numero inteiro"))
soma = 0
for contador in range (a):
    numero_sorteado = randint ( 1, 10)
    print(numero_sorteado)
    soma = soma + numero_sorteado
print( "Soma é:" , soma)
