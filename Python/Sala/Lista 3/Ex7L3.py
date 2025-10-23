"""7)- Exibir as potencias e 3 variando de 0 a 15. Deve ser considerado que
qualquer número elevado a zero é 1 e elevado a 1 é ele mesmo.
3 elevado a 0 = 1
3 elevado a 1 = 3
(...)
3 elevado a 15 = 14348907"""

print("Potências de 3")
for i in range (16):
    print(f"3 elevado a {i} = {3**i}")