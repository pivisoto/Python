def valida_senha_corrigido(senha):
    if len(senha) >= 7:
        upper_ok = any(char.isupper() for char in senha)
        lower_ok = any(char.islower() for char in senha)
        dig_ok = any(char.isdigit() for char in senha)
        return upper_ok and lower_ok and dig_ok
    
    senha = input("insira sua senha")
    while not valida_senha_corrigido(senha):
        print("senha invalida")
        senha = input("insira sua senha")
    print("senha valida")
