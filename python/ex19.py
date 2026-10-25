#Sorteio de nome de um aluno para apagar o quadro
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')

nomes = [nome1, nome2, nome3]

sorteio = random.choice(nomes)

print('O nome sorteado foi:', sorteio)