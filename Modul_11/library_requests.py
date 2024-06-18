import requests

# получение веб-страницы с помощью get-запроса
res = requests.get('https://api.github.com/events')
# узнаем кодировку
print(res.encoding)
print(res.headers)  # заголвки
print(res.status_code)  # статус запроса
# print(res.text) # текстовое содержимое
print(res.json()) # Содержимое ответа в JSON
# передача параметров в URL
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
