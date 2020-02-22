import csv
import show
import argparse
import numpy as np
import matplotlib.pyplot as plt

def dataset() :
	liste = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
	x = np.array([1] * 24, float)
	Y = np.array([1] * 24, float)
	Theta = np.random.randn(2, 1)
	for i in range(len(liste)) :
		if (i < 24):
			x[i] = liste[i][0]
			Y[i] = liste[i][1]
	x = x.reshape(x.shape[0], 1)
	Y = Y.reshape(Y.shape[0], 1)
	X = np.hstack((x, np.ones(x.shape)))
	normX = MinMaxScaler().fit_transform(X)
	# nx = (x - x.mean()) / x.std()
	# normX = np.hstack((nx, np.ones(nx.shape)))
	return x, X, normX, Y, Theta

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
	for i in range(0, n_iterations) :
		Theta = Theta - learning_rate * grad(X, Y, Theta)
		cost_history[i] = cost_function(X, Y, Theta)
	return Theta, cost_history


def ft_linear_regression() :
	x, X, normX, Y, Theta = dataset()
	learning_rate = 0.008
	n_iterations = 500
	final_Theta, cost_history = gradient_descent(normX, Y, Theta, learning_rate, n_iterations)
	# final_Theta = final_Theta * normX.std() - normX.mean()
	# final_Theta = (final_Theta - x.mean()) / x.std()
	# final_Theta[1] = 8481.172796984529
	# final_Theta[0] = -0.020129886654102203
	prediction = model(X, final_Theta)

	return x, Y, prediction, cost_history, final_Theta, n_iterations

def argument_parser() :
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--prediction", action="count", default=0, help="show the prediction curve")
	parser.add_argument("-ch", "--cost_history", action="count", default=0, help="show the cost history curve")
	parser.add_argument("-cd", "--coef_determination", action="count", default=0, help="show the coefficient determination")
	args = parser.parse_args()

	x, Y, prediction, cost_history, final_Theta, n_iterations = ft_linear_regression()

	if args.prediction >= 1 :
		show.prediction_curve(x, Y, prediction)
	elif args.cost_history >= 1 :
		show.cost_history_curve(n_iterations, cost_history)
	elif args.coef_determination >= 1 :
		show.coef_determination(Y, prediction)
	show.thetas_values(float(final_Theta[1]), float(final_Theta[0]))

if __name__ == '__main__' :
	argument_parser()