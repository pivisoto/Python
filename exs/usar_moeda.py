from moeda import *
moedas = int(input("insira a quantidade de moedas que voce possui "))
print("oque deseja fazer com elas? 1 - aumentar , 2 - diminuir , 3 - dobrar , 4 - dividir")
resposta = int(input())
if resposta == 1:
    print(aumentar(moedas + "R$"))
elif resposta == 2:
    print(diminuir(moedas + "R$"))
elif resposta == 3:
    print(dobro(moedas + "R$"))
elif resposta == 4:
    print(metade(moedas + "%.2f R$"))
else:
    print("você inseriu um numero invalido que não resulta em nenhuma operação")
    