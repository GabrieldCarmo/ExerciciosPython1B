i = 3
while i > 0:
    senha = int(input("Digite sua senha Usuário 001: "))
    if senha == 1234:
        print("Acesso permitido!!")
        i = 0
    else:
        i-=1
        if i > 0:
            print("Senha incorreta! Só te resta {} tentativas!".format(i))
        else:
            print("Conta Bloqueada!!")