#! /usr/bin/python3

# TODO: Permitir buscar só as mais tocadas ou todas as músicas

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
qtd = 15				# Buscar 15 primeiras musicas (padrão)

help_msg = "\nUSO: python " + os.path.basename(__file__) + " -b \"nome de uma banda\"\n\
			\nOpções:\n\
    -b  \"nome da banda\"   busca as músicas de uma banda.\n\
    -a  \"bandas.txt\"      permite ler a banda a partir de um arquivo\n\
    -v                    mostra a versão e sai\n\
    -h                    mostra esta mensagem de ajuda e sai\n"

def checa_params():
	""" Checa as opções da linha de comandos """

	try:
		opts, args = getopt.getopt(sys.argv[1:],"vhn:b:a")
		for opt, arg in opts:
			if opt == "-b":
				busca['q'] = arg.replace(" ", "-")

			elif opt == "-n":
				global qtd
				qtd = int(arg)

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

	except getopt.GetoptError:
	    print (help_msg)
	    sys.exit(2)

def version():
	""" Retorna a versão do programa extraída do cabeçalho """

	return 	"\n" + os.path.basename(__file__) +  " Ver: " + __version__ +
	"\n\nLicença " + __license__ + "\
	\nEste é um software livre: você é livre para alterá-lo e redistribuí-lo.\
	\nNÃO HÁ GARANTIA, na máxima extensão permitida pela lei\n"

def arquivo(arq):
	f = open(arq, 'rw', encoding="utf8")
	bandas = []

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
	# manda o Crawler fazer a busca
	v.crawler(busca, qtd)
	print('\n ------------------------------------------------------------- \n')

# ===========================================================================

if __name__ == "__main__":
	main_func() # Inicio do programa





# Fim
