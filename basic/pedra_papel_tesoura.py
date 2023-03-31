jogador1 = int(input( " Primeiro jogador, digite 0 para pedra, 1 para papel ou 2 para tesoura "))
jogador2 = int(input(" Segundo jogador, digite 0 para pedra, 1 para papel ou 2 para tesoura "))
pedra = 0
papel = 1 
tesoura = 2
if ( jogador1 == jogador2):
  print("Ninguém ganhou!")
elif ((jogador1 == pedra and jogador2 == tesoura) or (jogador1 == tesoura and jogador2 == papel) or (jogador1 == papel and jogador2 == pedra)):
  print("jogador 1 venceu!")
else:
  print("jogador 2 venceu!")