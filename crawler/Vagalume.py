import requests
from bs4 import BeautifulSoup

class Vagalume:
	""" Esta classe emcapsula o Crawler que extrai do site www.vagalume.com.br,
	informações de músicas de uma determinada banda  """

	def crawler(self, busca):
		""" Extrai as músicas da banda passada pelo url """

		url = 'https://www.vagalume.com.br/%(q)s/'
		r = requests.get(url % busca)
		soup = BeautifulSoup(r.text, "lxml")
		faixa = [title.text

		for title in soup.findAll('span', attrs={'itemprop':'name'})]

		for count, t in enumerate(faixa):
			print(format(count + 1, '02d') +')', t)
