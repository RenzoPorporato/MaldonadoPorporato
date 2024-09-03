from flask import Flask, render_template, request, redirect, url_for, session
from modules.Config import Config
from modules.procesar_datos import extraer_datos, ordenar_peliculas
from modules.manejar_resultados import guardar_resultado, cargar_resultados
from random import random


app = Flask(__name__)
app.config.from_object(Config)

frases_peliculas = extraer_datos('data/frases_de_peliculas.txt')
peliculas = ordenar_peliculas(frases_peliculas)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar_peliculas')
def listar_peliculas():
    return render_template('listar_peliculas.html', peliculas=peliculas)

@app.route('/iniciar_trivia', methods=['POST'])
def iniciar_trivia():
    usuario = request.form['usuario']
    num_frases = int(request.form['num_frases'])

    if num_frases < 3:
        return redirect(url_for('index'))
    
    session['usuario'] = usuario
    session['num_frases'] = num_frases
    session['frases'] = random.sample(frases_peliculas, num_frases)
    session['aciertos'] = 0

    return redirect(url_for('trivia'))

@app.route('/trivia')
def trivia():
    if 'frases' not in session or len(session['frases']) == 0:
        return redirect(url_for('index'))

    frase_actual = session['frases'].pop(0)
    opciones = random.sample(peliculas, 3)
    if frase_actual[1] not in opciones:
        opciones[random.randint(0, 2)] = frase_actual[1]

    session['frase_actual'] = frase_actual

    return render_template('trivia.html', frase=frase_actual[0], opciones=opciones)

@app.route('/verificar_respuesta', methods=['POST'])
def verificar_respuesta():
    respuesta = request.form['opcion']
    frase_actual = session['frase_actual']

    if respuesta.lower() == frase_actual[1].lower():
        session['aciertos'] += 1
        correcto = True
    else:
        correcto = False

    if len(session['frases']) == 0:
        guardar_resultado(session['usuario'], session['aciertos'], session['num_frases'])
        return redirect(url_for('resultado_final'))

    return render_template('resultado.html', correcto=correcto, respuesta_correcta=frase_actual[1])

@app.route('/resultado_final')
def resultado_final():
    return render_template('resultado_final.html', aciertos=session['aciertos'], total=session['num_frases'])

@app.route('/resultados')
def resultados():
    resultados = cargar_resultados()
    return render_template('resultados.html', resultados=resultados)

if __name__ == '__main__':
    app.run()