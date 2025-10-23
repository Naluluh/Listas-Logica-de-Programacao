"""6) Elaborar um programa que escreva em tela os números de 20 a 1, informando
quando eles são pares e quando são ímpares, utilizando o comando for( )."""

i = 20
while i > 0:
    if i % 2 == 0:
        print(f"{i} é um número par")
    else: 
        print(f"{i} é um númerp ímpar")
    i -= 1
