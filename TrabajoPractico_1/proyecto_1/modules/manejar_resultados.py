from datetime import datetime
import json

def guardar_resultado(usuario, aciertos, total, archivo='resultados.json'):
    nuevo_resultado = {
        "usuario": usuario,
        "aciertos": aciertos,
        "total": total,
        "fecha": datetime.now().strftime("%d/%m/%y %H:%M")
    }
    
    try:
        with open(archivo, 'r+', encoding='utf-8') as file:
            resultados = json.load(file)
            resultados.append(nuevo_resultado)
            file.seek(0)
            json.dump(resultados, file, indent=4)
    except FileNotFoundError:
        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump([nuevo_resultado], file, indent=4)

def cargar_resultados(archivo='resultados.json'):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []