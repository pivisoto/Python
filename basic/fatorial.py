n = int(input())#U x U - 1 x U - 2 x U - 3 x U - 4 ... U - n
f = 1
while n > 0:
  f = f * n
  n = n - 1
print (f)