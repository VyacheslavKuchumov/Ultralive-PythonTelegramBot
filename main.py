import requests
import json
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, request, jsonify
from SECRET import TOKEN

# Configure logging to save logs to a file with a maximum size and backup count.
handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def send_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=params)
    return json.loads(response.text)

app = Flask(__name__)

@app.before_request
def log_request_info():
    logger.info("Incoming Request: %s %s", request.method, request.path)
    logger.info("Headers: %s", request.headers)
    logger.info("Body: %s", request.get_data())

@app.route("/", methods=['GET'])
def test_page():
    return 'Bot is running🚀🚀🚀'

@app.route("/notify", methods=['POST'])
def notify_user_in_telegram():
    try:
        data = request.get_json()
        logger.info("Received JSON: %s", data)

        if not data or 'chat_id' not in data or 'message' not in data:
            logger.error("Invalid request data: %s", data)
            return jsonify({"error": "Invalid request data. Must include 'chat_id' and 'message'."}), 400

        chat_id = data['chat_id']
        message = data['message']

        if isinstance(chat_id, list):
            responses = []
            for single_chat_id in chat_id:
                try:
                    response = send_message(TOKEN, single_chat_id, message)
                    responses.append({"chat_id": single_chat_id, "status": "success", "response": response})
                except Exception as e:
                    logger.error("Error sending message to %s: %s", single_chat_id, str(e))
                    responses.append({"chat_id": single_chat_id, "status": "failed", "error": str(e)})
            return jsonify(responses), 200
        else:
            response = send_message(TOKEN, chat_id, message)
            return jsonify({"chat_id": chat_id, "status": "success", "response": response}), 200

    except Exception as e:
        logger.exception("An unexpected error occurred.")
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5378)
