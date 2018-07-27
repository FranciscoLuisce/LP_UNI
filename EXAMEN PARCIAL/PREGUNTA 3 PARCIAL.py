import random
n = random.randint(1,15)
A = []
B = []
N = ["*","R"]
print("Número de filas: ",n)
for i in range (0,n) :
    A.append([])
    for j in range (0,4) :
        valor = random.choice(N)
        A[i].append(valor)
for i in range (0,n) :
    B.append([])
    for j in range (0,4) :
        valor2 = random.choice(N)
        B[i].append(valor2)

print("Lado izquierdo:",A)
print("Lado derecho",B)
