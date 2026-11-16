#Faça um progarma que leia o nome completo e mostre eleem maiuscula minuscula e quantas letras tem sem contar os espaços e quantas letras tem o primeiro nome
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))