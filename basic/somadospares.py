num1 = int(input("Digite o numero inicial "))
num2 = int(input("Digite o numero final "))
soma = 0
for i in range(num1, num2+1):
  if i % 2 == 0:
    soma = soma + i
print( "a soma é:" , soma)

  
  
    