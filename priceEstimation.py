import json

def get_tetas_values() :
    with open("file.json", "r") as read_file:
        data = json.load(read_file)
    return data["teta0"], data["teta1"]

def price_estimation() :
    teta0, teta1 = get_tetas_values()
    km = input("Quel est le kilométrage de votre voiture ? ")
    price = teta0 + int(km) * teta1
    print("Votre voiture est estimée à " + str(price) + " euros.")


if __name__ == '__main__' :
    price_estimation()