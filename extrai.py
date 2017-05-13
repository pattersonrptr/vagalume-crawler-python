#! /usr/bin/python3

# TODO: Talvez deixar o usuário escolher uma música da lista
# e direcioná-lo para a página para escutá-la e, também, dar uma opção
# para que ele possa ver a letra e a tradução no terminal.

from bs4 import BeautifulSoup
from optparse import OptionParser

import requests
import sys

url = 'https://www.vagalume.com.br/%(q)s/'

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
		busca['q'] = input('>> Buscar: ')

def vagalume_crawler():
	r = requests.get(url % busca)
	soup = BeautifulSoup(r.text, "lxml")
	faixa = [title.text
	for title in soup.findAll('span', attrs={'itemprop':'name'})]

	for count, t in enumerate(faixa):
		print(str(count + 1)+')', t)

def buscar_novamente():
	op = input("Buscar novamente? ( S | N )").upper()

	if op != "N" and op != "S":
		print("Opção inválida:", op)
		buscar_novamente()

	return op

def main_func():
	checa_params()
	print("\nBuscando por", busca['q'].replace('-', ' ') + "...\n")
	vagalume_crawler()
	print('\n-----------------------------------------------------------\n')


# ===========================================================================

if __name__ == "__main__":
	main_func()






# Fim
