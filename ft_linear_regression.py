import json
import csv
from random import random
import numpy as np

def matrix_product(A, B):
    n = len(A); p = len(A[0]);  q = len(B[0])
    return [[sum([A[i][k]*B[k][j] for k in range(p)]) for j in range(q)] for i in range(n)]

def get_datas_values_from_csv() :
	liste = []
	# Fill list with our datas
	with open("data.csv") as fcsv:
		lecteur = csv.reader(fcsv)
		for ligne in lecteur:
			liste.append(ligne)
	return liste

def dataset() :
	liste = get_datas_values_from_csv()
	X = [ [ 1 for j in range(2) ] for i in range(24) ]
	Y = [1] * 24
	# Create random values for vector(a,b)
	T = [ random() for i in range(2) ]
	# Create vector Y and matrix X
	for i in range(len(liste)):
		if (i < 24):
			X[i][0] = int(liste[i + 1][0])
			Y[i] = int(liste[i + 1][1])
	return X, Y, T

def model(X, T) :
	return matrix_product(X, T)

def cost_function(X, Y, T) :
	m = len(y)
	return 1 / (2 * m) * ((model(X, T) - Y)**2) # Il faut faire la somme du dernier groupe entre paranthèse

def grad(X, Y, T) :
	m = len(y)
	return 1 / m * matrix_product(X, model(X, T) - Y) # Il faut faire la transposée de X ici

def gradient_descent(X, Y, T, learning_rate, n_iterations) :
	for i in range(0, n_iterations):
		T = T - learning_rate * grad(X, Y, T)
	return T

def print_tetas_values(teta0, teta1) :
	tetas = {
		"teta0": teta0,
		"teta1": teta1
	}
	with open("file.json", "w") as json_file:
		json.dump(tetas, json_file, indent=4)


def ft_linear_regression() :
	X, Y, T = dataset()
	print(T)
	print(T[0])
	print(T[1])
	final_T = gradient_descent(X, Y, T, learning_rate=0.001, n_iterations=1000)
	teta0 = final_T[0]
	teta1 = final_T[1]
	print_tetas_values(teta0, teta1)

if __name__ == '__main__' :
	ft_linear_regression()