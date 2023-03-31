def tamanho(quantidade):
    if len(quantidade) >= 7:
        print("a")
    else:
        print("senha invalida")

def caixa_alta(maiuscula):
    if maiuscula.isupper() == True:
        print("")
    else:
        print("senha invalida")
    
def caixa_baixa(minuscula):
    if minuscula.islower():
        print("")
    else:
        print("senha invalida")

def numeros(numero):
    if any(map(str.isdigit,numero)) == True:
        print("")
    else:
        print("senha invalida")

senha = input("insira sua senha")
tamanho(senha)
caixa_alta(senha)
caixa_baixa(senha)
numeros(senha)
