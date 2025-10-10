'''Ler dois valores A e B, efetuar a troca dos mesmos de forma que a variável A
passe a ter o valor da variável B e vice-versa. Exibir os valores trocados.'''



a = int(input("Insira o valor da primeira variável: "))
b = int(input("Insira o valor da segunda variável: "))

a,b = b,a

print(f"TROCA\nO vnovo valor da primeira variável é: {a} e o novo valor da segunda variável é: {b}\n")