import json
import matplotlib.pyplot as plt

def thetas_values(theta0, theta1) :
	thetas = {
		"theta0": theta0,
		"theta1": theta1
	}
	with open("file.json", "w") as json_file:
		json.dump(thetas, json_file, indent=4)

def prediction_curve(x, Y, prediction) :
	plt.scatter(x, Y)
	plt.plot(x, prediction, c='r')
	plt.show()

def cost_history_curve(i, cost_history) :
	plt.plot(range(i), cost_history)