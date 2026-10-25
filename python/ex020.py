# Crie uma ordem de apresentação do trabaçlho com os nomes dos alunbos sorteados
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nomme4 = input('Digite o quarto nome: ')

nomes = [nome1, nome2, nome3, nomme4]

sorteio = random.shuffle(nomes)
print('A ordem de apresentação será:\nPrimeiro: {}\nSegundo: {}\nTerceiro: {}\nQuarto: {}'.format(nomes[0], nomes[1], nomes[2], nomes[3]))