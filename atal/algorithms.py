# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas

def retorna_matriculas_decrescente(alist):
	left_index = 0
	right_index = len(alist) -1
	quick(alist, left_index, right_index)
	return alist
	
def quick(alist, left_index, right_index):
	if left_index < right_index:
		piv = partition(alist, left_index, right_index)
		quick(alist, left_index, piv - 1)
		quick(alist, piv + 1, right_index)
		
def partition(alist, left_index, right_index):
	i = left_index - 1
	pivot = alist[right_index]
	j = i + 1
	
	for j in xrange(i+1, len(alist)):
		if alist[j] > pivot:
			i = i +1
			swap(alist, i, j)
	
	swap(alist, i + 1, right_index)
	return i+1

def swap(alist, i, j):
	tmp = alist[i]
	alist[i] = alist[j]
	alist[j] = tmp
	
