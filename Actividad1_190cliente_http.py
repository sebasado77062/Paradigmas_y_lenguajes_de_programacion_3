import requests

url = "https://jsonplaceholder.typicode.com/posts"

miposteo = {
    "Ubicacion? ":"Arriba del jet ski",
    "Papoi? ":"Revoleado",
    "Mision? ":"Cumplida"
}

response = requests.get(url)
print(response.status_code)
print(response.headers["Content-Type"])
respuesta2daparte=requests.post(url, json=miposteo)
print(respuesta2daparte)
