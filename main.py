#! /usr/bin/python3

# TODO:  ADICIONAR OPÇÃO PARA LER O NOME DA BANDA EM UM ARQUIVO
# O arquivo pode conter o nome de várias bandas e artistas, separados por
# um em cada linha ou por um caractere corinda como | #  ou ;

# TODO: Talvez deixar o usuário escolher uma música da lista
# e direcioná-lo para a página para escutá-la e, também, dar uma opção
# para que ele possa ver a letra e a tradução no terminal.

from crawler.Vagalume import Vagalume
import sys

v = Vagalume()

args_l = len(sys.argv)
args = sys.argv
busca = dict()

def checa_params():
	if args_l >= 2:
		if args[1] == '-b' or args[1] == '--banda':
			if args_l > 2:
				busca['q'] = "-".join(args[2:])

			else:
				print("Erro: A opção ", args[1], "necessita parâmetros")
				exit(1)

		elif args[1] == '-h' or args[1] == '--help':
			print('\nUSO: %s -b nome de uma banda' % args[0])
			print('\nOpções:\n')
			print('-b, --banda          busca as músicas de uma banda.')
			print('-h, --help           mostra esta mensagem de ajuda e sai.')
			exit(0)
		else:
			print("Erro: Opção inválida ", args[1])
			exit(1)
	else:
		string = input('>> Buscar: ')
		busca['q'] = "-".join( string.split()  )

def main_func():
	checa_params()
	print("\nBuscando por", busca['q'].replace('-', ' ')
	.lower().title() + "...\n")
	v.crawler(busca)
	print('\n-----------------------------------------------------------\n')


# ===========================================================================

if __name__ == "__main__":
	main_func()






# Fim
