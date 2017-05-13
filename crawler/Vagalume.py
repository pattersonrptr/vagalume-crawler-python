""" Crawler que extrai uma lista de músicas do Vagalume """

import requests					# Para fazer requisições HTTP
from bs4 import BeautifulSoup	# Para extrair dados de arquivos HTML

class Vagalume:
	""" Esta classe emcapsula o Crawler que extrai do site www.vagalume.com.br,
	títulos de músicas de uma determinada banda  """

	def crawler(self, busca):
		""" Extrai as músicas da banda passada pelo url """

		url = 'https://www.vagalume.com.br/%(q)s/'
		r = requests.get(url % busca)
		soup = BeautifulSoup(r.text, "lxml")

		lista = soup.findAll('ol', attrs={'class' : 'artTops'})

		for element in lista:
			for count, span in enumerate( element.findAll('span') ):
				# print (span.text)
				print(format(count + 1, '02d') +')', span.text)

		'''
		faixa = [element
		# for title in soup.find_all('span',  attrs={ 'itemprop' : 'name' }) ]
		for element in soup.findAll('ol',  attrs={ 'class' : 'artTops' }) ]
		'''

		'''
		for element in faixa:
			print (element.findAll('span'))
		'''

		# print(len(span), 'resultados encontrados!')
		'''
		for count, t in enumerate(faixa):
			print(format(count + 1, '02d') +')', t)
		'''
