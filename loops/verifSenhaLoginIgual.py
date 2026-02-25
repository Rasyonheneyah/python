# Verificador se a senha é igual o nick de usuário!
print('Tela de login')
usuario=input('Digite o seu usuário: ')
senha=input('Digite sua senha: ')
while usuario==senha:
    senha=input('A senha não pode ser igual ao seu nome de usuário, digite outra senha:')
print('Logado com sucesso!')