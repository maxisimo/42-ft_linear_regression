import json
import csv
import numpy as np
import matplotlib.pyplot as plt

def dataset() :
	liste = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
	x = np.array([1] * 24, float)
	Y = np.array([1] * 24, float)
	Theta = np.random.randn(2, 1)
	for i in range(len(liste)):
		if (i < 24):
			x[i] = liste[i][0]
			Y[i] = liste[i][1]
	x = x.reshape(x.shape[0], 1)
	Y = Y.reshape(Y.shape[0], 1)
	X = np.hstack((x, np.ones(x.shape)))
	normX = (X - X.mean()) / X.std()
	return x, normX, Y, Theta

def model(X, Theta) :
	return X.dot(Theta)

def cost_function(X, Y, Theta) :
	m = len(Y)
	return 1 / 2 * m * np.sum((model(X, Theta) - Y)**2)

def grad(X, Y, Theta) :
	m = len(Y)
	return 1 / m * X.T.dot(model(X, Theta) - Y)

def gradient_descent(X, Y, Theta, learning_rate, n_iterations) :
	cost_history = np.zeros(n_iterations)
	for i in range(0, n_iterations):
		Theta = Theta - learning_rate * grad(X, Y, Theta)
		cost_history[i] = cost_function(X, Y, Theta)
	return Theta, cost_history

def print_thetas_values(theta0, theta1) :
	thetas = {
		"theta0": theta0,
		"theta1": theta1
	}
	with open("file.json", "w") as json_file:
		json.dump(thetas, json_file, indent=4)


def ft_linear_regression() :
	x, X, Y, Theta = dataset()
	final_Theta, cost_history = gradient_descent(X, Y, Theta, learning_rate=0.015, n_iterations=1000)
	prediction = model(X, final_Theta)
	# plt.plot(range(1000), cost_history)
	plt.scatter(x, Y)
	plt.plot(x, prediction, c='r')
	plt.show()
	print_thetas_values(float(final_Theta[0]), float(final_Theta[1]))

if __name__ == '__main__' :
	ft_linear_regression()