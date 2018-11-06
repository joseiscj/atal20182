#coding: utf-8

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda
def retorna_minimo_moedas(valor, tipos_moedas):
	print valor, tipos_moedas
	resultado = troco_guloso(tipos_moedas, valor)
	if resultado == sys.maxint:
		return -1
	else:
		return resultado

def retorna_minimo_moedas_FB(tipos_moedas, valor):
	if valor == 0:
		return 0

	resultado = sys.maxint

	for moeda in tipos_moedas:

		if (moeda <= valor):
			resultado = min(resultado, retorna_minimo_moedas_FB(tipos_moedas, valor - moeda) + 1)

	return resultado

def retorna_minimo_moedas_backtracking(tipos_moedas, valor):
	return retorna_minimo_moedas_BT(tipos_moedas, valor, [])

def retorna_minimo_moedas_BT(tipos_moedas, valor, possivel_solucao):
	tamanho_solucao = -1
	if eh_solucao(valor, possivel_solucao):
		return len(possivel_solucao)
	else:
		for i in range(len(tipos_moedas)):
			possivel_solucao.append(tipos_moedas[i])
			if eh_solucao_promissora(possivel_solucao, valor):
				tamanho = retorna_minimo_moedas_BT(tipos_moedas, valor, possivel_solucao)
				if tamanho_solucao == -1:
					tamanho_solucao = tamanho
				else:
					if tamanho_solucao >= tamanho:
						tamanho_solucao = tamanho
			possivel_solucao.pop()
	return tamanho_solucao

#
def eh_solucao(valor, moedas):
	soma = 0
	for i in range(len(moedas)):
		soma = soma + moedas[i]
	return soma == valor

def eh_solucao_promissora(possivel_solucao, valor):
	soma = 0
	for i in range(len(possivel_solucao)):
		soma = soma + possivel_solucao[i]
	return soma <= valor

#print retorna_minimo_moedas(30, [5,10,15])

# SOLUCAO GULOSA
def troco_guloso(moedas, valor):
	possivel_solucao = []
	value = 0
	while (not eh_solucao(valor, possivel_solucao)):
		if (not moedas):
			return -1
		valor_da_vez = max(moedas, key=int)
		possivel_solucao.append(valor_da_vez)
		if (eh_solucao_promissora(possivel_solucao, valor)):
			value = value + 1
		else:
			possivel_solucao.pop()
			moedas.remove(valor_da_vez)
	return value

print troco_guloso([1,4,2], 5)
