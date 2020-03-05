import json
import sys
import matplotlib.pyplot as plt

def thetas_values(theta0, theta1) :
	thetas = {
		"theta0": theta0,
		"theta1": theta1,
	}
	with open("thetas.json", "w") as json_file:
		json.dump(thetas, json_file, indent=4)
	print("Vector Theta as been successfully print in the file : thetas.json")
	print("\noptional arguments:")
	print("  -h, --help           show the help message and exit")
	print("  -p, --prediction     show the prediction curve")
	print("  -ch, --cost_history  show the cost history curve")
	print("  -cd, --coef_determination\n\t\t       show the coefficient determination")

def prediction_curve(x, Y, prediction) :
	plt.scatter(x, Y)
	plt.plot(x, prediction, c='r')
	plt.show()

def cost_history_curve(i, cost_history) :
	plt.plot(range(i), cost_history)
	plt.show()

def coef_determination(y, pred) :
	u = ((y - pred)**2).sum()
	v = ((y - y.mean())**2).sum()
	coef = 1 - u / v
	print("The determination coefficient is equal to : " + str(coef))
	sys.exit(0)