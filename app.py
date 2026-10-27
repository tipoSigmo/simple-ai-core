from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "message": "SimpleAi Cloud Engine Ready!"})

@app.route("/think", methods=["POST"])
def think():
    data = request.get_json(silent=True) or {}
    user_prompt = data.get("prompt", "")

    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    ai_response = f"[Cloud Engine]: Запрос «{user_prompt}» успешно обработан облачным сервером!"

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
