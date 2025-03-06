from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/crypto-webhook", methods=["POST"])
def crypto_webhook():
    data = request.json
    print("Pagamento Recebido:", data)  # Log para monitoramento
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
