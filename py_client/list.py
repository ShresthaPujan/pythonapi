import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done"
}
get_response = requests.get(endpoint,json=data) 
print(get_response.json())