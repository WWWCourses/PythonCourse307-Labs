import requests

payload = """{
      "title": "Learn PyQt",
      "completed": true,
      "id": 5
}"""

request_headers = {
	'content-type':'application/json'
}

response = requests.post('http://localhost:3000/todos', headers=request_headers, data=payload)

if(response.status_code == 201):
	print('Data saved sucessfully!')