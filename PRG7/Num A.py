
words = []
ans = ""
i = 0

while True:
	print("Enter '000' to execute program")
	ans = input("Enter characters or words to capitalize :")
	words.append(ans)
	if words[i] == "000":
		print("")
		print("Your Words:")
		print("")
		for word in words:
			print(word.upper())
		print("")
		input("Press enter to close")
		quit()
	else:
		i += 1