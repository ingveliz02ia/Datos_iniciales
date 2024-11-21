from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

# Variable para almacenar temporalmente el último nombre completo y correo electrónico recibido
latest_data = None
@app.route('/')
def form():
    return("Informacion de Datos Temporales")
# Endpoint para recibir datos
@app.route('/receive-data', methods=['POST'])
def receive_data():
    global latest_data
    # Obtén el JSON enviado en la solicitud
    data = request.get_json()
    
    if not data or "first_name" not in data or "last_name" not in data or "email" not in data or 'phone_number' not in data:
        return jsonify({"error": "Invalid JSON format. 'first_name' and 'email' are required."}), 400

    # Almacena solo el nombre completo y correo electrónico
    latest_data = {
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "phone_number":data["phone_number"]
    }
    print("Datos actualizados:", latest_data)

    return jsonify({"status": "Data received", "data": latest_data}), 200

# Endpoint para obtener el último dato
@app.route('/get-data', methods=['POST','GET'])
def get_data():
    if latest_data is None:
        return jsonify({"error": "No data available"}), 404

    # Devuelve el último dato almacenado
    return jsonify(latest_data), 200

if __name__ == '__main__':
    #app.run(port=6000, debug=True)
    serve (app, host='0.0.0.0', port=80)
