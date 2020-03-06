import json
import sys

def get_thetas_values() :
	try:
		with open("thetas.json", "r") as read_file:
			data = json.load(read_file)
	except:
		sys.exit(-1)
	return data["theta0"], data["theta1"]

def price_estimation() :
	theta0, theta1 = get_thetas_values()
	while(1):
		s = input("Wich mileage is on your car ? ")
		if not s:
			print('\nPlease enter a value')
		else:
			break
	try:
		assert(all([c in '-0123456789' for c in s]))
	except:
		print('\nPlease use a valid litteral value for int() with base 10.')
		sys.exit(-1)
	km_input = float(s)
	if km_input < 0:
		print("\nA mileage under 0 ?\n.\n.\n.\nReally ?")
		sys.exit(-1)
	if km_input >= 409764:
		print("\nYour price car is estimated at 0 euros or under.. You should not sell it.")
		sys.exit(-1)
	km = (km_input - 22899) / (240000 - 22899)
	price = theta0 + km * theta1
	print("\nYour price car is estimated at " + str(int(price)) + " euros.")


if __name__ == '__main__' :
	price_estimation()
