#faça um programa que leia algo pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
texto = str(input('Digite algo: ')).upper().strip()
print('A letra "A" aparece {} vezes.'.format(texto.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(texto.find('A') + 1))
print('A letra "A" aparece pela última vez na posição {}.'.format(texto.rfind('A') + 1))