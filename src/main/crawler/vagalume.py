""" Módulo Vagalume.
 contém a classe vagalume que implementa o Crawler."""

import requests                 # Para fazer requisições HTTP
from bs4 import BeautifulSoup   # Para extrair dados de arquivos HTML

class Vagalume:
	""" Esta classe emcapsula o Crawler que extrai do site www.vagalume.com.br,
	títulos de músicas de uma determinada banda  """


	def crawler(self, busca, qtd = 15, todas = False, musica = str()):
		""" Extrai as músicas da banda passada pelo url
		 	Recebe a busca, a quantidade a buscar (opicional)
			e se deve buscar todas (opicional) .
			Se a variável musica (opcional) não for vazia, então busca uma musica
			específica na lista de musicas.
		"""

		encontrou = False # Variável para verificar se encontrou musica específicada na linha de comandos

		url = 'https://www.vagalume.com.br/%(q)s/' # Prepara a URL de busca
		r = requests.get(url % busca)			   # Obtem a resposta do site com o HTML

		# Interpreta a resposta e retorna em forma de texto HTML para a variável soup
		soup = BeautifulSoup(r.text, "lxml")

		# Se passado argumento musica não vazio, busca por todas as musicas que
		# casem com a palavra fornecida
		if musica:
			# Busca na lista de todas as musicas
			lista = soup.findAll('ul', attrs = {'class' : 'tracks'})

			print('Resultado: ')

			# Exibe todas as musicas cujo nome contenha a palavra passada na variável musica
			# ou avisa que não encontrou nenhuma musica
			for element in lista:
				for count, span in enumerate( element.findAll('span') ):
					if musica.lower() in span.text.lower():
						print(format(count + 1, '02d') +')', span.text.title())
						encontrou = True

			if not encontrou:
				print('Não foi encontrada nenhuma musica com a palavra', musica.title())

			return

		# Se não buscar por musica específica mas pela lista de musicas

		# Se for definido todas, busca todas as musicas em lista normalmente
		if todas:
			lista = soup.findAll('ul', attrs = {'class' : 'tracks'})
		else: # Se não, então busca a lista das mais famosas (a lista com as 25 primeiras na página da banda no vagalume),
			  #  mas respeitando o limite 'qtd' cujo padrão é 15
			lista = soup.findAll('ol', attrs = {'class' : 'artTops'})

	    # Finalmente exibe a lista de musicas
		# Percorre o ResultSet lista, e para cada elemento encontrado que vai ser uma <ul> ou uma <ol>
		for element in lista:      # Busca por todos os elemetos <span> dentro de do elemento
			for count, span in enumerate( element.findAll('span') ):
				print(format(count + 1, '02d') +')', span.text)     # Exibe o conteúdo da <span> que deve ser o Nome da Musica
				if count + 1 == qtd:	 # Se atingir o limite fornecido pelo usuário ou o padrão 15
					break				 # termina o loop
