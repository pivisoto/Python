a = float(input("insira o valor de a "))
b = float(input("insira o valor de b "))
c = float(input("insira o valor de c "))
if (a == b == c):
  print ("o triângulo é equilátero ")
elif not (b - c < a):
  print (" não é possível formar um triângulo")
elif not ( a < b + c):
  print (" não é possível formar um triângulo")
elif not (a - c < b):
  print (" não é possível formar um triângulo")
elif not ( b < a + c):
  print (" não é possível formar um triângulo")
elif not (a - b < c):
  print (" não é possível formar um triângulo")
elif not (c < a + b):
  print (" não é possível formar um triângulo")
elif (a == b):
  print ("o triângulo é isósceles ", end='')
elif (a == c):
  print ("o triângulo é isósceles ", end='')
elif (c == b):
  print ("o triângulo é isósceles ")
else:
  print ("o triângulo é escaleno ")