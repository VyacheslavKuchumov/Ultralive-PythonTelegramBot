vera_id = 1701329648
vyachik_id = 1403125548
import requests
import json

# Replace with your bot token and recipient's chat ID

from SECRET import TOKEN

def send_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=params)
    return json.loads(response.text)

# Example usage:
message_text = "i dunno arab bruh спик руша or omericanmain"
response = send_message(TOKEN, vera_id, message_text)
print(response)
