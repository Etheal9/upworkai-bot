from flask import Flask, request
import requests

TOKEN = "7969019345:AAGzAuDEFM26hfrX1MDoVYQi69gL35k_58Y"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        requests.post(BASE_URL + "/sendMessage", json={"chat_id": chat_id, "text": f"You said: {text}"})
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
