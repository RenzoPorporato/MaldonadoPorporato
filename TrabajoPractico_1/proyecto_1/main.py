# Aplicación principal
from modules.Config import app

@app.route("/")
def prueba_saludo():
     pass


if __name__ == "__main__":      
     app.run(debug=True)

#Esto va al final, asumo que es para correr la aplicacion