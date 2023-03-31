lista1 = []
lista2 = []
lista3 = []

while True:
  n = str(input("insira um numero na lista "))
  if n != "":
    lista1.append(n)
  else:
    while True:
      a = str(input("insira um numero na lista2 "))
      if a != "":
        lista2.append(a)
      else:
        break
    break
int_lista1 = list(map(int,lista1))
int_lista2 = list(map(int,lista2))
for i in lista1:
  for c in lista2:
    if i == c:
      lista3.append(i)
int_lista3 = list(map(int,lista3))
print(int_lista3)


