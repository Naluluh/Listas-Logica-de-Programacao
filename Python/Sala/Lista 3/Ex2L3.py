"""2)- Exibir o total da soma obtido dos cem primeiros números inteiros
(1+2+3+4+5+.....+97+98+99+100)."""

soma = 0
for i in range (101):
    soma = soma + i
print(f"A soma dos números de 1 a 100 é {soma}")