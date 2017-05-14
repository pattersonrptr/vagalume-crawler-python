""" Módulo Vagalume.
 	contém a classe vagalume que implementa o Crawler."""

import requests                 # Para fazer requisições HTTP
from bs4 import BeautifulSoup   # Para extrair dados de arquivos HTML

class Vagalume:
	""" Esta classe emcapsula o Crawler que extrai do site www.vagalume.com.br,
	títulos de músicas de uma determinada banda  """


	def crawler(self, busca, qtd = 15, todas = False):
		""" Extrai as músicas da banda passada pelo url
		 	Recebe a busca, a quantidade a buscar (opcional)
			e se deve buscar todas (opcional) """

		url = 'https://www.vagalume.com.br/%(q)s/' # Prepara a URL de busca
		r = requests.get(url % busca)			   # Obtem a resposta do site com o HTML

		# Interpreta a resposta e retorna em forma de texto HTML para a variável soup
		soup = BeautifulSoup(r.text, "lxml")

		# Se for definido todas, busca as musicas em lista normalmente
		if todas:
			lista = soup.findAll('ul', attrs={'class' : 'tracks'})
		else: # Se não, então busca a lista das mais famosas (a lista com as 25 primeiras na página da banda no vagalume),
			  #  mas respeitando o limite 'qtd' cujo padrão é 15
			lista = soup.findAll('ol', attrs={'class' : 'artTops'})

	    # Finalmente exibe a lista de musicas

		# Percorre o ResultSet lista, e para cada elemento encontrado que vai ser uma <ul> ou uma <ol>
		for element in lista:      # Busca por todos os elemetos <span> dentro de do elemento
			for count, span in enumerate( element.findAll('span') ):
				print(format(count + 1, '02d') +')', span.text)     # Exibe o conteúdo da <span> que deve ser o Nome da Musica
				if count + 1 == qtd:	 # Se atingir o limite fornecido pelo usuário ou o padrão 15
					break				 # termina o loop
