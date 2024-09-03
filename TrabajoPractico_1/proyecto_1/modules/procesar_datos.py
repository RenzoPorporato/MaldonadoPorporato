import random

def extraer_datos(archivo):
    frases_peliculas = []
    with open(archivo, 'r', encoding='utf-8') as file:
        for linea in file:
            frase, pelicula = map(str.strip, linea.split(';'))
            frases_peliculas.append((frase.lower(), pelicula.lower()))
    return frases_peliculas

def ordenar_peliculas(frases_peliculas):
    peliculas = sorted(set([pelicula for _, pelicula in frases_peliculas]))
    return peliculas