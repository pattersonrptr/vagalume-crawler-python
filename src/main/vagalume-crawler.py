#! /usr/bin/python3

"""
	Programa principal. Implementa um Web Crawler que extrai e lista as
	músicas de uma determinada banda usando o site www.vagalume.com.br

    File name: vagalume_crawler.py
    Author: Patterson A. da Silva jr
    Date created: 13/05/2017
    Date last modified: 15/05/2017
    Python Version: 3.5.3
"""

import os                 # Para funções do sistema
import sys                # para sys.argv
sys.path.insert(0, '../') # /src

import getopt        # Para tratar as opções de linha de comandos
import unicodedata   # para remover acentos em strings
import re            # Para expressões regulares

from crawler.vagalume import Vagalume	# Importa o crawler do Vagalume

# Informações sobre o programa
__author__ = "Patterson A. da Silva jr"
__copyright__ = "Copyright 2017, "
__credits__ = ["Patterson A. da Silva jr"]
__license__ = "GPLv3+"
__version__ = "1.0.0"
__maintainer__ = "Patterson A. da Silva jr"
__email__ = "pattersonjunior@gmail.com"
__status__ = "Production"

args = sys.argv			# Argumentos recebidos da linha de comandos
args_l = len(sys.argv)	# Quantidade de argumentos passados
v = Vagalume()			# Crawler do Vagalume
busca = dict()			# Dicionário de busca
qtd = 15				# Quantidade a ser listada
todas = False			# Flase, lista só as mais tocadas, True Lista todas as musicas em ordem alfabética

nome_programa = os.path.basename(__file__).split('.')[0] # Obtém o nome do programa sem a extensão .py

# Mensagem de ajuda que é exibida sempre que passada a opção -h ou após uma menságem de erro
help_msg = "\nUSO: python " + nome_programa + " -b \"nome de uma banda\"\n\
			\nOpções:\n\
    -b  \"nome da banda\"                   busca as músicas de uma banda.\n\
    -a  \"bandas.txt\"                      permite ler a banda a partir de um arquivo\n\
    -t                                    Listar todas as musicas em ordem alfabética\n\
    -n                                    Quantidade de musicas a listar\n\
    -v                                    mostra a versão e sai\n\
    -h                                    mostra esta mensagem de ajuda e sai\n\n\
OBS. Nomes de bandas compostos por mais de uma palavra, devem ser\n \
     passados entre aspas, exemplo: \n \
     python " + nome_programa + " -b \"system of a down\"\n"

def checa_params():
	""" verifica e trata as opções da linha de comandos """

	try:
		# Define as opções que o programa pode receber e se recebem parâmetros
		opts, args = getopt.getopt(sys.argv[1:],"vhtn:b:a:")

		for opt, arg in opts:
			if opt == "-b":							# Recebe o nome da banda passado na linha de comandos
				busca['q'] = arg.replace(" ", "-")  # e substitui os espaços por hífens

			elif opt == "-n":
				global qtd			# Define a quantidade máxima de musicas a ser lida
				qtd = int(arg)		# recebe da linha de comandos

			elif opt == "-t":
				global todas		# Se passado -t na linha de comandos
				todas = True		# Lê todas as músicas e não só as mais conhecidas
									# respeitando o limite de 15 ou o que for passado pela opção -n

			elif opt == "-a":
				if '-b' not in sys.argv: # A opção -b tem prioridade sobre a -a
					arquivo( arg )		 # Exibe uma lista de nomes de bandas gravada num arquivo
										 # pede para o usuário escolher uma banda

			elif opt == "-v":
				print( version() )		# mostra a versão do programa e sai
				exit( 0 )

			elif opt == "-h":
				print(help_msg)			# Mostra Ajuda, Autor e versão, termina o programa em seguida
				print("Author: " + __author__)
				print( version() )
				exit(0)

	except getopt.GetoptError as err: # Se houver erro
		print ( str(err) )		      # Mostra o erro e uma mensagem de ajuda e finaliza o programa
		print (help_msg)			  # retornando código de erro 2.
		sys.exit(2)

def rm_acentos_e_chars_especiais(palavra):
	""" Transforma caracteres com acento em caracteres normais.
		Também remove caracteres especiais """

	# Unicode normalize transforma um caracter em seu equivalente em latin.
	nfkd = unicodedata.normalize('NFKD', palavra)
	palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
	# Regex para retornar a palavra apenas com números, letras e espaço
	return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

def version():
	""" Retorna a versão do programa """

	return 	"\n" + os.path.basename(__file__) +  " Ver: " + __version__ + "\n\nLicença " + __license__ + "\
	\nEste é um software livre: você é livre para alterá-lo e redistribuí-lo.\
	\nNÃO HÁ GARANTIA, na máxima extensão permitida pela lei\n"

def arquivo(arq):
	try:
		f = open(arq, 'r+', encoding="utf8")
	except IOError as err:
		print (str(err))
		exit(2)

	bandas = list()

	print()

	for i, line in enumerate(f):
		bandas.append(line)
		print(format(i + 1, '02d') +')', line.title())

	n_banda = int(input(' >> Número da banda a pesquisar: '))

	busca['q'] = bandas[n_banda - 1].strip().replace(" ", "-")

	f.close()

def main_func():
	""" Função principal que executa o programa todo. """

	# Checa opções de linha de comandos
	checa_params()
	# Se não foi passado a opção -b, lê do teclado
	if not busca:
		string = input('>> Buscar: ')
		busca['q'] = "-".join( string.split() )

	# Mesmo que o usuário digite 'SyStEm Of A dOwN' na busca, será exibido:
	# Buscando por System Of A Down...
	print("\nBuscando por", busca['q'].replace('-', ' ')
	.lower().title() + "...\n")

	busca['q'] = rm_acentos_e_chars_especiais(busca['q'])
	# manda o Crawler fazer a busca
	v.crawler(busca, qtd, todas)
	print('\n ------------------------------------------------------------- \n')

# ===========================================================================

if __name__ == "__main__":
	main_func() # Inicio do programa
