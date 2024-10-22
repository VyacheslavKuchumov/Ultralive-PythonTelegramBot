import ollama

qwen = 'qwen2.5-coder:7b'
mistral_nemo = "mistral-nemo:12b"

# response = ollama.chat(model=mistral_nemo, messages=[
# {
# 'role': 'user',
# 'content': 'Why is the sky blue?',
# },
# ])
#
# print(response['message']['content'])

paragraphs = ["Распиши введение дипломной работы по прогнозированию востребованности профессий", "Распиши ТЗ дипломной работы по прогнозированию востребованности профессий"]


for text in paragraphs:
    response = ollama.generate(model=mistral_nemo, prompt=text)
    print(response['response'])
