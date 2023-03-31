import random

numero1 = random.randrange(0,100)
numero2 = random.randrange(0,100)
escolha = str(input("escolha somar(S) ou multiplicar (M) "))
if (escolha == "S"):
  somar = numero1 + numero2
  print("a soma aleatoria é ", numero1 , "+", numero2 , "=" ,somar)
elif (escolha == "M"):
  multiplicar = numero1 * numero2
  print("a multiplicação aleatoria é " ,numero1 , "x", numero2 , "=" , multiplicar)
else: 
  print("o valor não foi encontrado")

