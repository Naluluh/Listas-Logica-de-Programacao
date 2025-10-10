'''13) Num laboratório de física, em uma experiência de Movimento Uniformemente
Variado, foram encontrados os seguintes valores: s0=2m, v0=3m/s, a=10m/s2.
Digitado o valor de t (segundos), apresentar em tela o valor de s (metros). Dada a
fórmula:
s = s0 + v0 . t + ½ . a . t2'''

t = float(input("Insira o tempo em segundos: "))
s = 2 + 3 * t + 0.5*10 *t*t

print(f"Movimento Uniformemente Variado: {s}m")