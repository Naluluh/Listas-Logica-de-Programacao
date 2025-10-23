"""5)- Exibir todos os números divisíveis por 4 que sejam menores que 200. Use a
instrução Se dentro da malha do programa. A variável Contador deverá iniciar
com o valor 1."""

print("Os números divisíveis por 4 são: (até 200)\n")
for i in range (201):
    if i % 4 == 0:
        print(i)