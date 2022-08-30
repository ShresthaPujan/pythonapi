import requests

endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"title": "Hello World"}) #Application programming interface
print(get_response.text)
print(get_response.status_code)
print(get_response.json())