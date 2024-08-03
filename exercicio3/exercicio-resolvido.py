"""
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros
"""
#In the following block, we will ask for the number of kilometers (km):
km = float(input('Enter the number of kilometers (km): '))

#In the next block, we will explain the conversion to meters, centimeters, and millimeters.
meters = km * 1000
centimeters = meters * 100
millimeters = centimeters * 10

#In the next block, we will display the conversion results on the screen:
print(f'{km} Kilometers equals {meters} meters, {centimeters} centimeters e {millimeters} millimeters')