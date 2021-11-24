# THIS IS VERY SECURE CODE
# create http server

# return """
#
# """

# ?userName=Ada&Password=1234
user_name = getRequestData('userName')
user_password = getRequestData('Password')

sql = """
	INSERT INTO users ('user_name', 'user_password') VALUES (user_name, user_password)
"""

return """
	HTTP/1.1 200 OK
	cache-control: no-cache
	content-encoding: gzip
	content-language: en-US
	content-type: text/html;charset=UTF-8
	date: Sat, 25 Sep 2021 08:48:45 GMT
	pragma: no-cache
	server: nginx
	strict-transport-security: max-age=31536000; includeSubDomains
	vary: Accept-Encoding
	x-frame-options: SAMEORIGIN

	<Welcome to my site, Ada>
"""


# USERS:
# id | user_name | user_password

