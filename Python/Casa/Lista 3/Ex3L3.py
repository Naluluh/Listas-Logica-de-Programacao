"""3) Elaborar um programa que escreva em tela os números de 1 a 20, informando
quando eles são pares e quando são ímpares, utilizando o comando while( )."""

i = 1
while i < 21:
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")
    i += 1