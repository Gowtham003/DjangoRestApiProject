import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
# endpoint = "http://localhost:8000/api/echo/"
putapiendopint = "http://localhost:8000/api/post/"

#response = requests.get(endpoint, data={"query": "Hello..."})
# response = requests.get(endpoint, params={"search":[1,2,3]}, json={"query": "Echo this Hello..."})
response = requests.post(putapiendopint, json={"title": "Test again", 'price': 120})

# print(response.text)
print(response.json())
print(response.status_code)