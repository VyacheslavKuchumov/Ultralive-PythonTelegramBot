
import requests

response = requests.post('http://localhost:5000/notify',
    json={
    'chat_id': 1403125548,
    'message': 'ЗАДАНИЕ НЕ ВЫПОЛНЕНО!!'})
print(response.status_code)
print(response.json())
