'''12) Elaborar um programa que receba, via teclado, os valores do espaço percorrido e
do tempo gasto por um veículo em movimento, para calcular e apresentar em tela sua
velocidade média.'''

d = float(input("Insira a distânca percorrida em quilômetros: "))
t = float(input("Insira o tempo gasto em horas: "))

vel = d / t

print(f"A velocidade média gasta durante o trajeto foi de {vel}km/h")