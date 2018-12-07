
num = 0

while num < 26:
	num += 1
	print(num)
	if num >= 25:
		ans = input("Would you like to restart counting?")
		if ans == "yes":
			num = 0
		else:
			print("Ok, fine")
			input("Press enter to close")
			quit()