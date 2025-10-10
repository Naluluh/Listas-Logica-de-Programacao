'''2) Crie um programa que permita fazer a conversão cambial entre Dólares e Reais.
Considere como taxa de câmbio US$1,00 = R$2,40. Leia um valor em Dólares pelo
teclado e mostre o correspondente em Reais.'''

dolar = float(input("Insira o valor em dólares: "))
real = dolar*2.4
print(f"--- CONVERSÃO CAMBIAL ---\nDólares: {dolar:.2f}\nReais: {real:.2f}")

