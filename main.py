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
import sys	# Para usar funções do SO e tratar opções de linha de comandos
import os	# Para paths

# TODO:  ADICIONAR OPÇÃO PARA LER O NOME DA BANDA EM UM ARQUIVO
# O arquivo pode conter o nome de várias bandas e artistas, separados por
# um em cada linha ou por um caractere corinda como | #  ou ;

# TODO:Permitir buscar mais do que 15 músicas

# TODO: Permitir buscar só as mais tocadas ou todas as músicas

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

def checa_params():
	""" Verifica as opções passados pela linha de comandos.
	Se não for passado uma opção, será pedido ao usuário que forneça a busca
	através de um input('>> Buscar: '). Também verifica se foi passado parâmetro
	inválido ou se faltou argumento para alguma opção.
	caso a função falhe, por falta de parâmetros ou opção inválida, termina o
	programa retornando erro ao sistema com a função exit( 1 )
	"""

	if args_l >= 2:
		if args[1] == '-b' or args[1] == '--banda':
			if args_l > 2:
				# O vagalume separa palavras por hífens na url de busca
				# Ex: https://www.vagalume.com.br/black-sabbath/
				busca['q'] = "-".join(args[2:])

			else:
				print("Erro: A opção ", args[1], "necessita parâmetros")
				exit(1)  # Sai e avisa o SO que houve um erro

		elif args[1] == '-n' or args[1] == '--number':
			if args_l > 2:
				try:
					val = int(args[2])
				except ValueError:
					print("Erro: A opção", args[1], "espera um número inteiro")
					exit(1)
			else:
				print("Erro: A opção ", args[1], "necessita parâmetros")
				exit(1)

		elif args[1] == '-a' or args[1] == '--arquivo':
			pass

		elif args[1] == '-V' or args[1] == '--version':
			print( version() )
			exit( 0 )

		elif args[1] == '-h' or args[1] == '--help':
			print('\nUSO: %s -b nome de uma banda' % args[0])
			print('\nOpções:\n')
			print('-b, --banda      busca as músicas de uma banda.')
			print('-a, --arquivo    permite ler a banda a partir de um arquivo')
			print('-V, --version    mostra a versão e sai.')
			print('-h, --help       mostra esta mensagem de ajuda e sai.')

			print( version() )

			exit(0) # Sai sem erro

		else:
			print("Erro: Opção inválida ", args[1])
			exit(1) # Sai e avisa o SO que houve um erro
	else:
		# Caso não o nome da banda não passado via linha de comando,
		# o usuário deve irnserí-lo via input()
		string = input('>> Buscar: ')
		busca['q'] = "-".join( string.split()  )

def version():
	""" Retorna a versão do programa extraída do cabeçalho """

	return 	"\n" + os.path.basename(__file__) +  " Ver: " + __version__ + "\n\nLicença " + __license__ + "\
	\nEste é um software livre: você é livre para alterá-lo e redistribuí-lo.\
	\nNÃO HÁ GARANTIA, na máxima extensão permitida pela lei\n"


def arquivo():
	# TODO
	""" Lê uma banda de um arquivo """
	pass


def main_func():
	""" Função principal que executa o programa todo. """

	# Checa opções de linha de comandos
	checa_params()
	# Mesmo que o usuário digite 'SyStEm Of A dOwN' na busca, será exibido:
	# Buscando por System Of A Down...
	print("\nBuscando por", busca['q'].replace('-', ' ')
	.lower().title() + "...\n")
	# manda o Crawler fazer a busca
	v.crawler(busca)
	print('\n-----------------------------------------------------------\n')

# ===========================================================================

if __name__ == "__main__":

	main_func() # Inicio do programa

# Fim
