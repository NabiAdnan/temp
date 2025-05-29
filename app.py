from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def home():
    return "🌾 Crop Recommendation API is running!"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received data:", data)

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    temperature = data.get("temperature")
    humidity = data.get("humidity")

    # Recommendation logic
    if temperature is not None and humidity is not None:
        if temperature > 30 and humidity > 70:
            crops = ["Rice", "Sugarcane"]
        elif temperature < 25 and humidity < 50:
            crops = ["Wheat", "Barley"]
        else:
            crops = ["Maize", "Millet"]

        return jsonify({
            "temperature": temperature,
            "humidity": humidity,
            "recommended_crops": crops
        })
    return jsonify({"error": "Missing temperature or humidity"}), 400

if __name__ == '__main__':
    app.run()
