import requests

endpoint = "http://localhost:8000/api/products/30002/"

response = requests.get(endpoint)

# print(response.text)
print(response.json())
print(response.status_code)