#Lab 5B Vignesh Peddi
#PROMPT: Seach csv file with birthday and give info
import csv
records = 0
search_count = 0
it_check = 0
lname = []
fname = []
birthday = []
with open("Z:\\lab5_updated.txt") as csvfile:
  file = csv.reader(csvfile)
  for rec in file:
    records += 1
    lname.append(rec[0])
    fname.append(rec[1])
    birthday.append(rec[2])
  found = -1
  loop = input("Would you like to run my code[y/n]: ")
  while loop == "y":

    search = input("Enter the birthday of the person you are searching for: ")
    listlength = len(birthday)

    for i in range(0, listlength):
        search_count += 1
        if search == birthday[i]:
          found = i
    
    if found >= 0:
        birthday1 = birthday[found]
        year = int(birthday1.split("/")[2])
        age = 2020 - year
        print("{0:10} {1:10} {2:10} {3:10}".format(lname[found],fname[found],birthday[found],age))
        print("The system took",search_count,"search iterations to find the person")
        search_count = 0
    else:
        print("You didn't enter the current birthday ")
    loop = input("Would you like to run my code[y/n]: ")



