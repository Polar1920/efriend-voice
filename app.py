import sys
sys.stdout.reconfigure(encoding='utf-8')

from flask import Flask, render_template, request, send_file
from gradio_client import Client

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Obtener el mensaje del formulario de la solicitud
    message = request.form["message"]
    
    # Crear una instancia del cliente para el nuevo modelo
    client = Client("LordCoffee/Multilingual-TTS")
    
    # Realizar la predicción con el nuevo modelo
    result = client.predict(
        text=message,
        language_code="English",
		speaker="Jenny",
		tashkeel_checkbox=False,
		api_name="/text_to_speech_edge"
    )
    
    # Retornar el archivo de audio como resultado
    return send_file(result[1], mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)
