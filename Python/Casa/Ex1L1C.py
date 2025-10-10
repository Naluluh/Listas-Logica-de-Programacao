'''1) Crie um programa que permita fazer a conversão cambial entre Reais e Dólares.
Considere como taxa de câmbio US$1,00 = R$2,40. Leia um valor em Reais pelo
teclado e mostre o correspondente em Dólares.'''

real = float(input("Insira o valor em reais: "))
dolar = real / 2.4

print(f"---CONVERSÃO CAMBIAL ---\nReais: {real:.2f}\nDólares: {dolar:.2f}")
