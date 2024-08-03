'''Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''

litros = float(input("Digite a quantidade de litros de combustível consumidos: "))
distancia = float(input("Digite a distância percorrida em quilômetros: "))

consumo_medio = distancia / litros

print("Consumo médio (km/l):", consumo_medio)