notas = int(input())
notas_100 = notas/100 
resto100 = notas % 100
notas_50 = resto100/50
resto50 = resto100 % 50
notas_20 = resto50/20
resto_20 = resto50 % 20
notas_10 = resto_20/10
resto10 = resto_20 % 10
notas_5 = resto10/5
resto5 = resto10 % 5
notas_2 = resto5/5
resto2 = resto5 % 2
notas_1 = resto2/1
if 0 < notas < 1000000:
    print("",notas,"\n",int(notas_100), " nota(s) de R$ 100,00\n",int(notas_50), " nota(s) de R$ 50,00\n",int(notas_20), " nota(s) de R$ 20,00\n",int(notas_10)," nota(s) de R$ 10,00\n",int(notas_5), " nota(s) de R$ 5,00\n", int(notas_2)," nota(s) de R$ 2,00\n",int(notas_1) , " nota(s) de R$ 1,00")
else: 
    print("Presentation Error")