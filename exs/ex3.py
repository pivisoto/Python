nome = str(input("insira o nome "))
data_nascimento = int(input("insira o ano de nascimento "))
carteira_de_trabalho = int(input("insira seu CTPS (caso não possua insira 0) "))
ano_contratacao = int(input("insira o ano de contratação (caso não possua insira 0) "))
salario = int(input("insira o salario (caso não possua insira 0) "))
idade = 2022 - data_nascimento

if (carteira_de_trabalho > 0):
    rh = {"nome":nome,"idade":idade,"carteira de trabalho":carteira_de_trabalho,"ano de contratação":ano_contratacao,"salário":salario,"idade de aposentadoria": + ano_contratacao - 2022 + 35 + idade}
    print(rh)
else :
    rh_pessoanova = {"nome":nome , "idade":idade,"idade de aposentadoria":idade + 35}
    print(rh_pessoanova)

#levando em conta a regra antiga do minimo de 35 anos de trabalho sem idade minima para aposentadoria