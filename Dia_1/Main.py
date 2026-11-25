import requests

url = "http://127.0.0.1:5500/"

response = requests.get(url)

print("Status: ", response.status_code)

print("Headers: ")
for nome, valor in response.headers.items():
    print(nome, ":", valor)

print("\n Resposta")
print(response.text[:500])