f1 = open("files/notas.txt", "r")
f2 = open("files/notas_sem_atrasos.txt", "r")
nota1 = []
nota2 = []
soma1 = 0
soma2 = 0
for i in f1:
    nota1.append(int(f1.readline()))
for i in f2:
    nota2.append(int(f2.readline()))
for x in nota1:
    soma1 += nota1[x]
for x in nota2:
    soma2 += nota2[x]
soma1 = soma1 / len(nota1)
soma2 = soma2 / len(nota2)
print("O valor completo é: " + str(soma1) + "\nO valor sem os modulos em atraso é: " + str(soma2))
print()
input('Prima enter para fechar.')