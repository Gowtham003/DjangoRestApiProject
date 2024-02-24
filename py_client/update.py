import requests

endpoint = "http://localhost:8000/api/products/10/update/"
data = {'title': "Test update", 'price': 400}
response = requests.put(endpoint, json=data)

# print(response.text)
print(response.json())
print(response.status_code)