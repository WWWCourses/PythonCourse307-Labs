# curl -X GET "https://api.chucknorris.io/jokes/random" -H "accept: application/json" -H "content-type: application/json"
import requests


request_headers = {
	'accept':'application/json',
	'content-type':'application/json'
}
response = requests.get('https://api.chucknorris.io/jokes/random', headers=request_headers)

if(response.status_code == 200):
	# print(response.text)
	data = response.json()
	print( data['value'] )

