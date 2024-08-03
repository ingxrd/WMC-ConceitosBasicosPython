"""
Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão
"""

# capturando a entrada do usuário dos 2 números
numero1 = int(input('Insira o 1º número: '))
numero2 = int(input('Insira o 2º número: '))

#um print para quebra de linha
print()
print(f'A SOMA de {numero1} + {numero2} é {numero1 + numero2}') #faço a soma diretamente no print e mostro também quais números o usuário digitou
print(f'A SUBTRAÇÃO de {numero1} - {numero2} é {numero1 - numero2}')
print(f'A MULTIPLICAÇÃO de {numero1} x {numero2} é {numero1 * numero2}')
print(f'A DIVISÃO de {numero1} / {numero2} é {numero1 / numero2:.2f}') #.:2f é para formatar a saida em somente 2 casas decimais. 
print()