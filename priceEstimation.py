import json

def get_thetas_values() :
    with open("thetas.json", "r") as read_file:
        data = json.load(read_file)
    return data["theta0"], data["theta1"]

def price_estimation() :
    theta0, theta1 = get_thetas_values()
    km = input("Quel est le kilométrage de votre voiture ? ")
    price = theta0 + int(km) * theta1
    # price = price * -0.000003418
    # price = price / -292576.841
    print("Votre voiture est estimée à environ " + str(int(price)) + " euros.")


if __name__ == '__main__' :
    price_estimation()
