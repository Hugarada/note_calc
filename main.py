f = open("files/notas.txt", "r")
nota = []
nota_all = []
soma1 = 0
soma2 = 0
ic = 0
for i in f:
    ic += 1
    nota_all.append(int(f.readline()))
    if nota_all[ic - 1] >= 10:
        nota.append(nota_all[len(nota_all) - 1])
for x in nota_all:
    soma1 += nota_all[x]
for j in nota:
    soma2 += nota[j]
soma1 = soma1 / (len(nota_all) - 1)
soma2 = soma2 / (len(nota) - 1)
print("O valor completo é: " + str(soma1) + "\nO valor sem os modulos em atraso é: " + str(soma2))
print()
input('Prima enter para fechar.')