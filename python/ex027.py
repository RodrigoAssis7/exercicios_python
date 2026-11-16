#faça um progarama que leia o nome cpmpleto de umapessoa mostrando o primeiro e o último nome separadamente
nome=str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print(f'Primeiro nome: {separado[0]}')
print(f'Último nome: {separado[-1]}')