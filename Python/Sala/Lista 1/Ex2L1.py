'''Ler uma temperatura em graus Fahrenheit e exibi-la convertida em graus
Centígrados, com a fórmula: C <- (((F-32) * 5) / 9), onde F é a temperatura em
Fahrenheit e C em Centígrados.'''

fahrenheit = float(input("Insira a temperatura em graus Fahrenheit: "))
celsius = (((fahrenheit-32)*5)/9)
print(f"--- CONVERSÃO ---\nGraus Fahrenheit: {fahrenheit:.2f}\nGraus Celsius: {celsius:.2f}\n")