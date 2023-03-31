x , y = list(map(int,input().split(" ")))
if (x == 1):
  preco = 4 * y
elif (x == 2):
  preco = 4.5 * y
elif (x == 3):
  preco = 5 * y
elif (x == 4):
  preco = 2 * y
elif (x == 5):
  preco = 5 * y
print (f"Total: R$ %.2f" %(preco))
        
        

