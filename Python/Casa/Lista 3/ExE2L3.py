"""Extra II) Escreva um programa para mostrar na tela os resultados de uma tabuada de um
número qualquer fornecido via teclado.
Exemplo:
Digite o número para a tabuada: 5 <Enter>
Tabuada do 5:
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50"""

a = int(input("Insira o valor da tabuada: "))
print(f"TABUADA DO {a}\n")
for i in range(11):
    resultado = a * i
    print(f"{a} X {i} = {resultado}")

