import requests

# url = 'https://bnr.bg/hristobotev/radioteatre/list'
url = 'https://www.imdb.com/chart/moviemeter/'

# r = requests.request('get', url, **kwargs)
query = {
	'ref_':'nv_mv_mpm'
}
headers = {
	'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
	'referer':'https://wwwcourses.github.io/'
}
r = requests.get(url, params=query, headers=headers)
# if r.status_code<400:
if r.ok:
	print(r.headers)
print(r)