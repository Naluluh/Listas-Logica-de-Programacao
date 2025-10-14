"""3) Calcule quantos azulejos são necessários para azulejar uma parede. É necessário
conhecer a altura da parede (AP), a sua largura (LP), e a altura do azulejo (AA) e sua
largura (LA). Leia os dados através do teclado."""

ap = float(input("Insira a altura da parede:"))
lp = float(input("\nInsira a largura da parede: "))
aa = float(input("\nInsira a altura do azulejo: "))
la = float(input("\nInsira a largura do azulejo: "))

areaP = ap*lp
areaA = aa*la

numA = areaP/areaA

print(f"\nQUANTIDADE DE AZULEJOS\nSerão necessários {numA:.0f} azulejos")


