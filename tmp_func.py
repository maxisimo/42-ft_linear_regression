import json
import csv

def get_tetas_values() :
    with open("file.json", "r") as read_file:
        data = json.load(read_file)
    return data["teta0"], data["teta1"]

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

def somme(i, teta0, teta1, x, y) :
	s = 0
	for k in range(1, i + 1):
		if (i < 24):
			s += teta0 + (teta1 * x[i] - y[i])
	return s

def calc_tetas_values() :
	ratio = 0.1
	teta0, teta1 = get_tetas_values()
	x, y = get_datas_values_from_csv()
	m = len(x)
	teta0 = ratio * ((1 / m) * somme(m, teta0, teta1, x, y))
	for i in range(len(x)):
		teta1 = ratio * ((1 / m) * somme(m, teta0, teta1, x, y) * x[i])
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