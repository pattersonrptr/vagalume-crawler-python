""" Crawler que extrai uma lista de músicas do Vagalume """

import requests					# Para fazer requisições HTTP
from bs4 import BeautifulSoup	# Para extrair dados de arquivos HTML

class Vagalume:
	""" Esta classe emcapsula o Crawler que extrai do site www.vagalume.com.br,
	títulos de músicas de uma determinada banda  """


	def crawler(self, busca, qtd = 15, todas = False):
		""" Extrai as músicas da banda passada pelo url """

		url = 'https://www.vagalume.com.br/%(q)s/'
		r = requests.get(url % busca)
		soup = BeautifulSoup(r.text, "lxml")

		if todas == True:
			lista = soup.findAll('ul', attrs={'class' : 'tracks'})
		else:
			lista = soup.findAll('ol', attrs={'class' : 'artTops'})


		for element in lista:
			for count, span in enumerate( element.findAll('span') ):
				print(format(count + 1, '02d') +')', span.text)
				if count + 1 == qtd:
					break
