#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor
numero = int(input('digite um valor: '))
sucessor = numero + 1
antecessor = numero - 1 
print('O sucessor de {} sera {} e seu antecessor sera {}.'.format(numero, sucessor, antecessor))