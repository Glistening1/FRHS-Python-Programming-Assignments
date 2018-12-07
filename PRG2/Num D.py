
list = []
i = 0

while True:
	list.append(int(input("Enter a number: ")))
	if list[i] == 000:
		average = sum(list) / len(list)
		print("The average of your list is = ", round(average, 2))
		input("Press enter to close")
		quit()
	else:
		i += 1