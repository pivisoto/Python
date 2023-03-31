produto = int(input("valor do produto = "))
escolha = int(input("escolha a forma de pagamento : a vista PIX,dinheiro ou cheque (1)/ a vista crédito (2)/ 2 parcelas crédito (3)/ 3 ou mais parcelas crédito (4) "))
if (escolha == 1):
  print ("o valor a ser pago é ", produto * 0.9)
elif (escolha == 2):
  print ("o valor a ser pago é ", produto * 0.95)
elif (escolha == 3):
  print ("o valor a ser pago é ", produto )
elif (escolha == 4):
  print ("o valor a ser pago é " ,produto * 0.80)

                   