import requests
from bs4 import BeautifulSoup

def crawler(url, busca):
	r = requests.get(url % busca)
	soup = BeautifulSoup(r.text, "lxml")
	faixa = [title.text
	for title in soup.findAll('span', attrs={'itemprop':'name'})]

	for count, t in enumerate(faixa):
		print(str(count + 1)+')', t)
