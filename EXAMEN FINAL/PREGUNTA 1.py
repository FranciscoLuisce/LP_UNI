#Componemos 5 funciones
def abrir_archivo():
    # Abrimos los archivos y los recorremos
    alumnosFile = open("alumno.csv")
    notasFile = open("notas.csv")
    cursosFile = open("curso.csv")

    #Leemos la primera línea, mas no la metemos en el arreglo porque no la necesitamos
    lineaAlumnos=alumnosFile.readline()
    lineaNotas=notasFile.readline()
    lineaCursos=cursosFile.readline()

    #Definimos los arreglos, aquí se meteran los elementos de los archivos enlistados.
    A=[]
    N=[]
    C=[]

    while lineaAlumnos!="":
        lineaAlumnos=alumnosFile.readline()
        x=lineaAlumnos.split(";")
        x.pop(len(x) - 1)
        A.append(x)
    A.pop(len(A)-1)#Eliminación del último elemento
    alumnosFile.close()

    #Análogamente con el resto de archivos
    while lineaNotas!="":
        lineaNotas=notasFile.readline()
        x=lineaNotas.split(";")
        x.pop(len(x)-1)
        N.append(x)
    N.pop(len(N)-1)
    notasFile.close()

    while lineaCursos!="":
        lineaCursos=cursosFile.readline()
        x=lineaCursos.split(";")
        x.pop(len(x) - 1)
        C.append(x)
    C.pop(len(C)-1)
    cursosFile.close()

    #En este arreglo meteremos toda la data procesada
    D=[]
    D.append(A)
    D.append(N)
    D.append(C)
    return D

def procesar_archivos(X):
    lista_alumnos=[]

    #Modificamos el índice 1, que almacena las notas, de la lista original D y le añadimos el nombre del curso respectivo
    for i in range(len(X[1])):
        for j in range(len(X[2])):
            if X[1][i][1]==X[2][j][0]:
                X[1][i].append(X[2][j][1])

    #Creamos una nueva lista llamada alumno y le añadimos los códigos de los alumnos y los nombres de los alumnos, los cuales están en la lista D
    for i in range(len(X[0])):
        alumno = []
        cod_alumno = X[0][i][0]
        nomb_alumno = X[0][i][1]
        alumno.append(cod_alumno)
        alumno.append(nomb_alumno)
        lista_alumnos.append(alumno)

    #Hacemos una lista auxiliar llamada aux alumnos que nos guarde el codigo de curso y la nota de ese curso de un determinado alumno
    for i in range(len(X[0])):
        aux_cursos=[]
        for j in range(len(X[1])):
            if lista_alumnos[i][0]==X[1][j][0]: #Aquí se verifica que alumno es
                z = X[1][j][1:len(X[1][j])]
                aux_cursos.append(z)
        lista_alumnos[i].append(aux_cursos)

    #El arreglo lista_alumnos fue añadiendo dentro de si las demás listas que se generaron en cada iteración for
    return lista_alumnos

def mostrar_datos(X):
    for i in range(len(X)):
        print("Alumno: ",X[i][1],"\nCódigo: ",X[i][0], "\nCursos: ")
        for j in range(len(X[i][2])):
            print(X[i][2][j][2],"con código:",X[i][2][j][0]," y con nota:",X[i][2][j][1])
        print("----------------\nSiguiente alumno\n----------------")

def promedio(X):
    #El proceso clásico para hallar promedios
    notas_alumno=X
    sum=0
    for i in range(len(notas_alumno)):
        sum+=int(notas_alumno[i][1])
    if len(notas_alumno)>0:
        prom=sum/len(notas_alumno) #Este len nos indica el número de cursos que lleva, asumiendo que todos pesan 1
    else:
        prom=0
    return prom

def imprimir_promedio(datos):
    # Esta lista es para poder mostrar el texto en archivos luego
    text=[]

    # Lista de promedios
    promedios=[]
    for i in range(len(datos)):
        x=promedio(datos[i][2]) #Recordar que la posición 2 de la lista ya fue modificada
        promedios.append(x)

    #Añadimos las líneas a la lista
    for i in range(len(datos)):
        linea=[]
        linea.append(datos[i][0])
        linea.append(datos[i][1])
        linea.append(str(promedios[i]))
        linea.append("\n")
        text.append(linea)

    #Creamos el archivo que mostrará el promedio
    promediosFile=open("prom.txt","w")
    #Añadimos la cabecera
    promediosFile.write("Código Nombre Promedio\n")
    for i in range(len(text)):
        for j in range(len(text[i])):
            promediosFile.write(" " + text[i][j] + " ")
    promediosFile.close()

#Llamamos a todas las funciones
val=abrir_archivo()
data=procesar_archivos(val)
imprimir_promedio(data)
mostrar_datos(data) #Esta función muestra los alumnos, los cursos que lleva y sus notas.