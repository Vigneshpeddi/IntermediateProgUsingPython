#Lab 6A Vignesh Peddi
#PROMPT: Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  
#VARIABLE DICTIONARY
#records               counts the records in the file
#binary_code           counts how many times the binary search performs the loop 
#lname                 LIST stores the last names of everyone in the file
#fname                 LIST stores the first name of everyone in the file
#dob                   LIST stores the dob of everyone in the list
#loop                  controls the loop to continuouslly run the program
#min                   min value of binary search(index)
#max                   max value of binary search(index)
#guess                 guess for the search determines next max/min
#search                what user is searching for
#BASE PROGRAM CODE
import csv#importing csv library
records = 0
binary_code = 0
lname = []
fname = []
dob = []
with open("Z:\\lab6A.txt") as csvfile: 
    file = csv.reader(csvfile)
    for rec in file:
        records += 1
        lname.append(rec[0])
        fname.append(rec[1])
        dob.append(rec[2])
    loop = "y"
    while loop == "y":
        min = 0#setting min value for bianry search
        max = records - 1#setting max value for binary search
        guess = int((min + max) / 2)#setting guess value for binary search
        search = input("Enter the Last Name: ")
        while (min < max and search != lname[guess]):#setting loop that runs untill search term is foudn or thew whole file has been searched
            binary_code += 1
            if search < lname[guess]:
                max = guess - 1#if the search value is less than the name at index value guess recalc max
            else:
                min = guess + 1#if the search value is less than the name at index value guess recalc min
            guess = int((min + max) / 2)#recalculate middle value
        if search == lname[guess]:
            print("The person with the last name",search,"was found and has the first name of",fname[guess],",last name of",search,",date of birth of",dob[guess])
            print("Search Count:",binary_code)
        else:
            print("The person with the last name",search,"was not found.")
            print("Search Count:",binary_code)
        loop = input("Continue: ")

     