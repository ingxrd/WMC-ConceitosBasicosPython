"""
Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
comer = input('Qual sua comida preferida? ')
sonho = input('Me diga, qual o seu maior sonho? ')

print(f'Prazer em te conhecer, {nome}! São {idade} anos muito bem vividos, hein! Tenho certeza que logo você realizará seu sonho de {sonho} e vai comer bastante {comer} para comemorar!!!')