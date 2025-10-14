'''10) Elaborar um programa para receber valores, via teclado, nas variáveis "a" e "b".
Após isto, o programa, utilizando-se de uma 3a. variável "c", deverá trocar o conteúdo
das variáveis "a" e "b".'''


a = int(input("Insira o valor da primeira variável: "))
b = int(input("Insira o valor da segunda variável: "))

c = a
a = b
b = c

print(f"--- TROCA ---\nO novo valor da primeira variável é: {a} e o novo valor da segunda variável é: {b}\n")