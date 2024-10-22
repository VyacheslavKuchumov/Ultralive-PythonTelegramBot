vera_id = 1701329648
vyachik_id = 1403125548
import requests
import json

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


from flask import Flask, request

app = Flask(__name__)

## Принимаем chat_id и message например с неактора
@app.route("/notify", methods=['POST'])
def notify_user_in_telegram():
    data = request.get_json()
    response = send_message(TOKEN, data['chat_id'], data['message'])
    print(f"Received POST data: {data}")
    return response, 200
