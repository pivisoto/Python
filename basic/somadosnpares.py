n1 = int(input("digite um valor inicial "))
n2 = int(input("digite o valor final "))
soma = 0 
while n1 <= n2:
  if n2 % 2 == 0:
    soma = soma + 1
  n1 = n1 + 1
print (f'soma é {soma}')