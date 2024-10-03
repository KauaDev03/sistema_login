print('Digite um usuário e uma senha para se cadastrar: ')
login = str(input('Usuário: '))
senha = str(input('Senha: '))
tentativas = 3

while True:
    loginAcessar = str(input('Digite seu login para acessar sua conta: '))
    senhaAcessar = str(input('Digite sua senha para acessar a sua conta: '))

    if loginAcessar == login and senhaAcessar == senha:
        print('Logado com sucesso!')
        break
    else:
        print('Usuario ou senha invalido!')
        tentativas -= 1
        if tentativas > 0:
            print(f'Você tem mais {tentativas} tentativas antes de bloquear')

        else:
            for c in range(1, 4):
                print('Seu acesso foi bloqueado!!!')
            break

        

