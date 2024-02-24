import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "Testing generic create"}
response = requests.post(endpoint, json=data)

# print(response.text)
print(response.json())
print(response.status_code)