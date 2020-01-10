import json
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

def dataset() :
	liste = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
	x = np.array([1] * 24, float)
	Y = np.array([1] * 24, float)
	# x, Y = make_regression(n_samples = 100, n_features = 1, noise = 10)
	Teta = np.random.randn(2, 1)
	for i in range(len(liste)):
		if (i < 24):
			x[i] = liste[i][0]
			Y[i] = liste[i][1]
	x = x.reshape(x.shape[0], 1)
	Y = Y.reshape(Y.shape[0], 1)
	X = np.hstack((x, np.ones(x.shape)))
	return x, X, Y, Teta

def model(X, Teta) :
	return X.dot(Teta)

def cost_function(X, Y, Teta) :
	m = len(Y)
	return 1 / 2 * m * np.sum((model(X, Teta) - Y)**2)

def grad(X, Y, Teta) :
	m = len(Y)
	return 1 / m * X.T.dot(model(X, Teta) - Y)

def gradient_descent(X, Y, Teta, learning_rate, n_iterations) :
	cost_history = np.zeros(n_iterations)
	for i in range(0, n_iterations):
		Teta = Teta - learning_rate * grad(X, Y, Teta)
		cost_history[i] = cost_function(X, Y, Teta)
	return Teta, cost_history

def print_tetas_values(teta0, teta1) :
	tetas = {
		"teta0": teta0,
		"teta1": teta1
	}
	with open("file.json", "w") as json_file:
		json.dump(tetas, json_file, indent=4)


def ft_linear_regression() :
	x, X, Y, Teta = dataset()
	final_Teta, cost_history = gradient_descent(X, Y, Teta, learning_rate=0.01, n_iterations=1000)
	prediction = model(X, final_Teta)
	plt.plot(range(1000), cost_history)
	# plt.scatter(x, Y)
	# plt.plot(x, prediction, c='r')
	plt.show()
	# teta0 = final_Teta[0]
	# teta1 = final_Teta[1]
	# print_tetas_values(teta0, teta1)

if __name__ == '__main__' :
	ft_linear_regression()