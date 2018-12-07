
numlist = []

for i in range(1,6):
	numlist.append(int(input("Enter in a number: ")))

numlist.sort(reverse=True)

print("")
for j in numlist:
	print("(%s)".center(40) % j)

print("")
input("Press enter to close")
