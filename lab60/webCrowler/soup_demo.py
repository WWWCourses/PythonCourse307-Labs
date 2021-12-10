from bs4 import BeautifulSoup as bs


def read_html(filename):
	with open(filename, 'r') as f:
		html = f.read()
		return html


html = read_html('./lib/data/simple.html')

soup = bs(html, 'html.parser')
# print(soup)

# child1 = soup.div.div
# print(child1)
# print(child1.parent.children)

# print(soup.div)
# print('~'*20)
# for div in soup.find_all('div'):
# 	print(div.string)


# print(soup.find_all('div', id="ch1"))

main = soup.find('div', id='main')

# TODO: make it work
children = (list(main.children)[0]).children




