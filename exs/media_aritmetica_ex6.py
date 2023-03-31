media_str = []
while True:
    a = input("insira os numeros para fazer a media aritmetica ")
    if a != "":
        media_str.append(a)
    else:
        break
media_int = list(map(int,media_str))
soma_da_media = sum(media_int)
print(soma_da_media/len(media_int))

