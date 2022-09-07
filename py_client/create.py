import requests


headers = {'Authorization': 'Bearer 147e6e479a00e923074f054866aed8f134306b41'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())