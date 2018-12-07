
import math

choice = 0
ans = 0
length = 0
width = 0
hypotenuse = 0
radius = 0

while True:
	print("""
	1. Calculate Circumference of Circle
	2. Calculate Area of Circle
	3. Calculate Circumference of a Square
	4. Calculate Area of Square
	5. Calculate Circumference of a Triangle
	6. Calculate Area of Triangle
	7. Exit
	""")
	choice = input("What would you like to calculate? ")
	if choice == "1":
		radius = input("Please enter a radius: ")
		ans = 2 * math.pi * float(radius)
		print("The circumference of the circle is " + str(ans))
	elif choice == "2":
		radius = input("Please enter a radius: ")
		ans = math.pi * float(radius) * float(radius)
		print("The area of the circle is " + str(ans))
	elif choice == "3":
		length = input("Please enter a length: ")
		ans = float(length) * 4
		print("The circumference of the square is " + str(ans))
	elif choice == "4":
		length = input("Please enter a length: ")
		width = input("Please enter a width: ")
		ans = float(length) * float(width)
		print("The area of the square is " + str(ans))
	elif choice == "5":
		length = input("Please enter a length: ")
		width = input("Please enter a width: ")
		hypotenuse = input("Please enter a hypotenuse: ")
		ans = float(length) + float(width) + float(hypotenuse)
		print("The circumference of the triangle is: " + str(ans))
	elif choice == "6":
		length = input("Please enter a base: ")
		width = input("Please enter a height: ")
		ans = (1/2) * float(length) * float(width)
		print("The area of the triangle is " + str(ans))
	elif choice == "7":
		quit()