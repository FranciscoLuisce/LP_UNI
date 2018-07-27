n = int(input("Número de almacenes: "))
m =[]
p =[]
q = []
if n < 21 and n > 0 :

    for i in range (0,n) :
        suma = 0
        print ("¿Cuántos productos hay en el almacén ",i+1,"?")
        valor = int(input())
        if valor > 0 and valor < 16 :
            m.append(valor)
            for j in range (0,valor):
                print ("¿Cuánto del producto ",j+1," hay?")
                valor2 = int(input())
                p.append(valor2)
                suma += valor2
            q.append(suma)
        else :
            print ("Número de productos no permitido.")
    for i in range (0,n) :
        print("En el almacén ", i + 1, " hay ", m[i], " productos.")

        for j in range (0,m[i]) :
            print ("En el almacén ",i+1," hay ", p[j], " unidades de producto ", j+1, ".")
        p.remove(p[0])
        print("En total de productos en el almacén ", i + 1, " es ", q[i], ".")
else :
    print ("Número de almacenes excede al permitido.")