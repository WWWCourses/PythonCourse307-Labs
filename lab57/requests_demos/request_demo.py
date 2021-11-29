import requests


api_endpoint = 'https://api.jokes.one'

#GET /jod/categories


# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
# requests.request('Get', api_endpoint+'/jod/categories',)
request_headers = {
	'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
	'accept':'text/html,application/json,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
response = requests.get(api_endpoint+'/jod/categories', headers=request_headers)
print(response.status_code)
# print(response.headers)
print(response.text)

