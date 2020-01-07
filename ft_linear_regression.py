import json
import csv

def get_datas_values_from_csv() :
	liste = []
	x = [1] * 24
	y = [1] * 24
	with open("data.csv") as fcsv:
		lecteur = csv.reader(fcsv)
		for ligne in lecteur:
			liste.append(ligne)
	for i in range(len(liste)):
		if (i < 24):
			x[i] = int(liste[i + 1][0])
			y[i] = int(liste[i + 1][1])
	return x, y

def calc_tetas_values() :
	x, y = get_datas_values_from_csv()
	teta0 = 0
	teta1 = 0
	return teta0, teta1

def print_tetas_values(teta0, teta1) :
	tetas = {
		"teta0": teta0,
		"teta1": teta1
	}
	with open("file.json", "w") as json_file:
		json.dump(tetas, json_file, indent=4)


def ft_linear_regression() :
	teta0, teta1 = calc_tetas_values()
	print_tetas_values(teta0, teta1)

if __name__ == '__main__' :
	ft_linear_regression()