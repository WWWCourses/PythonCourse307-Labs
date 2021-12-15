from bs4 import BeautifulSoup
import re

html = '''
<div class="date">
	обновено на 17.05.21 в 08:15
</div>
<div class="date">
	<span class="sound_icon"></span> публикувано на 23.03.21 в 13:34
</div>
'''

soup = BeautifulSoup(html, "html.parser")
date_rx = re.compile(r'(\d{2}\.\d{2}\.\d{2})')

date_divs = soup.find_all('div', class_="date")
for div in date_divs:
	# print("\n\n",div)
	# print(div.string)
	# print(div.contents)

	m = date_rx.search(str(div))
	if m:
		pub_date = m[1]
		print(pub_date)
		# pub_date = datetime.datetime.strptime(pub_date, "%d.%m.%y")


