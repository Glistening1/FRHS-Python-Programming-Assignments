
import os

clear = lambda: os.system('cls')
check = ""
addUser = ""
namelist = ["Lydie", "Suelle", "Esca", "Logy", "Firis", "Sophie"]
idslist = ["1", "2", "3", "4", "5", "6"]

while True:
  for name, ids in zip(namelist, idslist):
    print("Name :" + name + " || ID: " + str(ids))

  print("")
  check = input("Enter a name or ID: ")
  if check in namelist:
    print("That student's ID is: " + str(idslist[namelist.index(check)]))
    print("")
    input("Press enter to clear")
    print("")
    clear()
  elif check in idslist:
    print("That student's name is: " + str(namelist[idslist.index(check)]))
    print("")
    print("")
    input("Press enter to clear")
    print("")
    clear()
  else:
    print("")
    addUser = input("That name or ID was not found in the database, would you like to add someone? ")
    if addUser.capitalize() == "YES" or addUser.capitalize() == "Y":
      namelist.append(input("Enter a name :"))
      idslist.append(input("Enter an ID :"))
      clear()
    else:
      clear()