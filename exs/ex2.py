from random import randint
jogador1 = randint(1,6)
jogador2 = randint(1,6)
jogador3 = randint(1,6)
jogador4 = randint(1,6)
ranking = {"player_vermelho":jogador1, "player_amarelo":jogador2, "player_azul":jogador3, "player_preto":jogador4}
for ordem in sorted(ranking,key = ranking.get, reverse=True):
    print(ordem, ranking[ordem])