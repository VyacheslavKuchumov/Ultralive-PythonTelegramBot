import requests
import json

from flask import Flask, request, jsonify
# # Replace with your bot token and recipient's chat ID

from SECRET import TOKEN

def send_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=params)
    return json.loads(response.text)



app = Flask(__name__)

@app.route("/", methods=['GET'])
def test_page():
    return 'Bot is running🚀🚀🚀'

## Принимаем chat_id и message например с неактора
@app.route("/notify", methods=['POST'])
def notify_user_in_telegram():
    try:
        # Retrieve and validate JSON data
        data = request.get_json()
        if not data or 'chat_id' not in data or 'message' not in data:
            return jsonify({"error": "Invalid request data. Must include 'chat_id' and 'message'."}), 400

        chat_id = data['chat_id']
        message = data['message']

        # Check if chat_id is a list for multiple users or a single ID
        if isinstance(chat_id, list):
            # Handle multiple chat IDs
            responses = []
            for single_chat_id in chat_id:
                try:
                    response = send_message(TOKEN, single_chat_id, message)
                    responses.append({"chat_id": single_chat_id, "status": "success", "response": response})
                except Exception as e:
                    responses.append({"chat_id": single_chat_id, "status": "failed", "error": str(e)})
            return jsonify(responses), 200
        else:
            # Handle single chat ID
            response = send_message(TOKEN, chat_id, message)
            return jsonify({"chat_id": chat_id, "status": "success", "response": response}), 200

    except Exception as e:
        # General error handling for unexpected issues
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)