nome = input('Digite um nome: ')
sobrenome = input('Digite o sobrenome: ')
idade = int(input('Qual a idade? '))
ano_de_nacimento = int(input('Qual ano nasceu? '))
e_maior_de_idade = idade >= 18
altura = float(input('Quantos metros de altura: '))

print('SEU NOME E: {}\nSEU SOBRENOME E: {}\nSUA IDADE E: {}\nNASCEU EM: {}\nE MAIOR DE IDADE? {}/n SUA ALTURA E: {}'.format(nome, sobrenome, idade, ano_de_nacimento, e_maior_de_idade, altura))