
complete = False

def Test():
    print("")
    q1 = input("There are 1030 books in the library. We bought 67 more books for the library. How many books are there in the library now?")

    if int(q1) == 1097:
        print("Correct, Move On.")
        print("")
        q2 = input("1085 girls and 531 boys took part in an art competition. How many students took part in the competition altogether?")
        
        if int(q2) == 1616:
            print("Correct, Move On.")
            print("")
            q3 = input("Margret sold 1392 meatballs on Friday. She sold 1940 more meatballs on Saturday than on Friday. How many meatballs did she sell on Saturday?")

            if int(q3) == 3332:
                print("Correct, Move On.")
                print("")
                print("You completed all of them! Congrats!")
                input("Press enter to close.")
                quit()
            else:
                print("Sorry, try again:")
                print("")

        else:
             print("Sorry, try again:")
             print("")

    else:
        print("Sorry, try again:")
        print("")

while True:
    Test()
    if complete == True:
        break
