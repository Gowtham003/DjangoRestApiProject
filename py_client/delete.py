import requests

endpoint = "http://localhost:8000/api/products/5/delete/"
response = requests.delete(endpoint)

# print(response.text)
print(response.status_code, response.status_code==204)