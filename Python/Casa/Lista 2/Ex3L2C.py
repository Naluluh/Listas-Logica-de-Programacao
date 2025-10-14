'''3) Uma Universidade tem problemas com arredondamento das médias dos alunos, 
pois cada professor estipula um critério de arredondamento. Devemos elaborar um 
programa, em Linguagem C++, para a secretaria da Universidade, resolvendo esse 
problema. O programa deve solicitar uma nota e fazer o devido arredondamento.
Regras:
Notas que ultrapassem 0,5 de resto serão arredondas para CIMA.
Ex: 4,6 –>5,0
Notas que abaixo ou igual a 0,5 de resto serão arredondas para BAIXO.
Ex: 4,5 –> 4,0'''


print("ARREDONDAMENTO DE NOTA")
nota = float(input("Insira a nota: "))
 
if nota < 5:
    novaNota = nota + 1
    print(f"{nota:.2f} foi arrendondado para {novaNota:.0f},0")

else: 
    novaNota = nota - 1
    print(f"{nota:.2f} foi arredondado para {novaNota:.0f},0")
