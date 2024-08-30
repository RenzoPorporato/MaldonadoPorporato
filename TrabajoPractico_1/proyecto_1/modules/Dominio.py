import random 

def extraer_datos (nombre_archivo):
    with open (nombre_archivo,"r") as archi:
        datos=list()
        for i in archi:
            fras,peli=i.split(";")
            datos.append([fras.strip().lower(),peli.strip().lower()])
    return datos
#Saco la informacion del archivo

def ordenar_datos (matriz):
    datos_ordenados=sorted(matriz,key=lambda x:x[1])
    return datos_ordenados
#ordeno alfabeticamente la matriz

def asociar_frases (matriz):
    frases_peliculas={}
    for i in matriz:
        frases[i[0]]=i[1]
    return frases_peliculas
#Se crea un diccionario donde cada frase tiene asociada una pelicula#

#De aca para abajo es para obtener una pelicula correcta mezclada con incorrectas
frases_peliculas=asociar_frases(extraer_datos("NOMBRE ARCHIVO"))
frases=list(frases_peliculas.keys())#Arma una lsita con las frases sacadas del diccionario
frase_seleccionada= random.choice(frases)#Saca una frase al azar
pelicula_correcta= frases_peliculas[frase_seleccionada]#Guarda la pelicula asociada a esa frase

def trivia (pelicula_correcta, peliculas_ordenadas):    
    opciones=[pelicula_correcta]#Crea una lista empezando con la pelicula correcta
    while len(opciones)<3:
        pelicula=random.choice(peliculas_ordenadas)
        if pelicula != pelicula_correcta and pelicula not in opciones:
            opciones.append(pelicula)
    random.shuffle(opciones)
    return opciones





    
    
    
