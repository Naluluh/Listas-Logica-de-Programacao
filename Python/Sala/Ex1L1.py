'''1)- Calcular a quantidade de litros de combustível gasta numa viagem, utilizandose um automóvel que faz 12Km por litro. Para obter o cálculo, o usuário deverá
fornecer o tempo gasto na viagem e a velocidade média durante a mesma. Assim,
será possível calcular a distância percorrida com a fórmula: DISTÂNCIA <-
TEMPO * VELOCIDADE. Tendo o valor da distância, calcule a quantidade de litros
de combustível usada na viagem com a fórmula: LITROS_USADOS <-
DISTÂNCIA / 12. O programa deverá exibir os valores da velocidade média, tempo
gasto na viagem, a distância percorrida e a quantidade de litros usada na viagem.'''

tempo = float(input("Insira o tempo da viagem (horas): "))
velocidade = float(input("Insira a velocidade média atingida durante a viagem (km/h): "))
distancia = tempo * velocidade
litrosUsados = distancia / 12

print(f"--- INFORMAÇÕES GERAIS DA VIAGEM ---\nTempo (h): {tempo:.2f}\nVelocidade Média (km/h): {velocidade:.2f}\nDistância (km): {distancia:.2f}\nCombustível Utilizado (L): {litrosUsados:.2f}\n")
