def extraer_datos (nombre_archivo):
    with open (nombre_archivo,"r") as archi:
        datos=list()
        for i in archi:
            fras,peli=i.split(";")
            datos.append([fras.strip().lower(),peli.strip().lower()])
    return datos
#Saco la informacion del archivo

def listar_peliculas (nombre_archivo):
    with open (nombre_archivo,"r") as archi:
        lista_peliculas=sorted(list())
        for i in archi:
            fras,peli=i.split(";")
            lista_peliculas.append(peli.strip().lower)
    return lista_peliculas
#Funcion que crea una lista que solo contiene las peliculas 

def ordenar_datos (matriz):
    datos_ordenados=sorted(matriz,key=lambda x:x[1])
    return datos_ordenados
#ordeno alfabeticamente la matriz

def asociar_frases (matriz):
    frases={}
    for i in matriz:
        frases[i[0]]=i[1]
    return frases
#Se crea un diccionario donde cada frase tiene asociada una pelicula