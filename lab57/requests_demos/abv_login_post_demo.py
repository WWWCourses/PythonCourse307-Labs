import requests

# payload = {
#       "username":'abc_test_abc',
# 	  "password":'qazw1234'
# }


payload = {
	's':'9D32D0B464C54F0B8FD17626D4C15599.passport1'
}

# request_headers = {
# 	'content-type':'application/json'
# }

url = 'https://nm60.abv.bg/email/login?s=9D32D0B464C54F0B8FD17626D4C15599.passport1'
response = requests.get(url)
print(response.status_code)

# if(response.status_code == 201):
# 	print('Data saved sucessfully!')