
import requests

response = requests.post('http://localhost:5000/notify',
    json={
    'chat_id': 1403125548,
    'message': 'ТЕСТОВОЕ СООБЩЕНИЕ таск "абвгд" не сделан!!!'})
print(response.status_code)
print(response.json())
