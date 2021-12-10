import re
import  requests
import threading

class Crawler():
	def __init__(self, seed):
		self.seed = seed
		self.data_path = './data/'

	def make_filename(self,url):
		""" Extracts domain from a url.
			Prepend data_path and append '.html'

			:param url: string

			return `domain`.html string
		"""
		rx = re.compile(r'^https?:\/\/(?:www\.)?([^\/]+)')
		m = rx.search(url)
		if m:
			# print(m[1])
			return self.data_path + m[1] + '.html'
		else:
			print(f'Can not match regex, url: {url}')
			exit(-1)


	def write_to_file(self,filename, content):
		""" Write string to given filename
				:param filename: string
				:param content: sring
		"""
		with open(filename, 'w') as f:
			try:
				f.write(content)
			except Exception:
				print(f'Can not write in file: {filename}')

	def get_html(self,url):
		""" Make GET request and save content to file
			First try with SSL verification (default),
			if error => disable SSL verification

			:param url: string
		"""
		try:
			r = requests.get(url)
		except requests.RequestException:
			# skip the SSL verification. Note, this is not a good practise, but just nasty workaround
			r = requests.get(url, verify=False)
		except Exception:
			print('Oops, something went wrong!')
			exit(-1)

		if r.ok:
			content = r.text

		filename = self.make_filename(url)
		self.write_to_file(filename, content)

	def run(self):
		""" run the crawler for each url in seed
			Use multithreading for each GET request

		"""
		for url in self.seed:
			tr = threading.Thread(target=self.get_html(url), daemon=True)
			tr.start()
			# self.get_html(url)


if __name__ == '__main__':
	seed = [
		'https://www.autokelly.bg/',
		'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm',
		'https://bnr.bg/hristobotev/radioteatre/list',
		'https://bnr.bg/lyubopitno/list',
		'https://www.jobs.bg/front_job_search.php?add_sh=1&from_hp=1&keywords%5B%5D=python',
		'https://bnr.bg/lyubopitno/list'
	]
	crawler = Crawler(seed)
	crawler.run()