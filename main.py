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

from crawler.Vagalume import Vagalume	# Importa o crawler do Vagalume
import getopt
import sys
import os

import unicodedata
import re

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

help_msg = "\nUSO: python " + os.path.basename(__file__) + " -b \"nome de uma banda\"\n\
			\nOpções:\n\
    -b  \"nome da banda\"   busca as músicas de uma banda.\n\
    -a  \"bandas.txt\"      permite ler a banda a partir de um arquivo\n\
    -t                    Listar todas as musicas em ordem alfabética\n\
    -n                    Quantidade de musicas a listar\n\
    -v                    mostra a versão e sai\n\
    -h                    mostra esta mensagem de ajuda e sai\n\n\
OBS. Nomes de bandas compostos por mais de uma palavra, devem ser\n \
     passados entre aspas, exemplo: \n \
     python " + os.path.basename(__file__) + " -b \"system of a down\"\n"

def checa_params():
	""" Checa as opções da linha de comandos """

	try:
		opts, args = getopt.getopt(sys.argv[1:],"vhtn:b:a:")
		for opt, arg in opts:
			if opt == "-b":
				busca['q'] = arg.replace(" ", "-")

			elif opt == "-n":
				global qtd
				qtd = int(arg)

			elif opt == "-t":
				global todas
				todas = True

			elif opt == "-a":
				if '-b' not in sys.argv: # A opção -b tem prioridade sobre a -a
					arquivo( arg )

			elif opt == "-v":
				print( version() )
				exit( 0 )

			elif opt == "-h":
				print(help_msg)
				print("Author: " + __author__)
				print( version() )
				exit(0)

	except getopt.GetoptError as err:
		print ( str(err) )
		print (help_msg)
		sys.exit(2)

def rm_acentos_e_chars_especiais(palavra):
	# Unicode normalize transforma um caracter em seu equivalente em latin.
	nfkd = unicodedata.normalize('NFKD', palavra)
	palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

	# Usa expressão regular para retornar a palavra apenas com números, letras e espaço
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

	for i, line in enumerate(f):
		bandas.append(line)
		print(format(i + 1, '02d') +')', line)

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





# Fim
