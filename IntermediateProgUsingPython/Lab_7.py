#Lab 7 Vignesh Peddi
#Prompt: Depending on how the user wants to search, you may need to sort the searched-through list before performing Binary Search.  Binary Search should be used for Menu Options 1 (First Name) and 2 (ID codes)  and the full record for the individual searched should be included if found (the user should be alerted if the person cannot be found).  If the user chooses options 3 or 4, you must print a list of everyone and their full record that fits the searched item (think: sequential search!) that has that Last Name or Allegiance.  Use the GOT_bubble_sort_7.txt file (you may change the name if you wish but you may NOT edit the text file outside of checking for and deleting empty end records).  The user should be able to search as many times as they would like.  If the user enters an option that does not exist, the program must tell them this before asking if the user would like to search for a new record
# import only system from os 
from os import system, name 
import random
  

def goodbye():#goodbye function for extra credit
    print("Goodbye, Winter is Coming")
def doitagain():#continue searching function that allows you to keep searching
    d = input("Would you like to do it again[y/n]: ")
    while d != "Y" and d != "y" and d != "N" and d != "n":
        d = input("Would you like to do it[y/n]: ")
    return d

def clear(): #function that completely wipes the screen
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 


#a function that swaps values for bubble sorting
def swap(n, j):

    t = n[j]
    n[j]= n[j + 1]
    n[j + 1] = t

#a function that allows a user to choose what to search by
def search_menu():

    print("1. Search by FIRST NAME")
    print("2. Search by ID")
    print("3. Search by LAST NAME")
    print("4. Search by ALLEGIANCE")
    print("5. EXIT")

    response = int(input("Please enter your choice [1 - 5]: "))

    while response != 1 and response != 2 and response != 3 and response != 4 and response != 5:#only accepting answers 1-5

        print("*ERROR*ERROR*")
        response = int(input("Please enter your choice [1 - 5]: "))
    return int(response)

def fnamesort(j):#sorting fucntion for first name
    for i in range(0, num_rec - 1):#outer loop

        for index in range(0, num_rec - 1):#inner loop

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
            if(fname[index] > fname[index + 1]):
            #if above is true, swap places!
            #temp = name[index]
            #name[index] = name[index + 1]
            #name[index + 1] = temp
                swap(fname, index)

            #swap all other values
            #temp = age[index]
            #age[index] = age[index + 1]
            #age[index + 1] = temp
                swap(age, index)
                swap(lname, index)
                swap(id, index)
                swap(allegiance, index)
def idsort(j):#sorting fucntion by id
    for i in range(0, num_rec - 1):#outer loop

        for index in range(0, num_rec - 1):#inner loop

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
            if(id[index] > id[index + 1]):
            #if above is true, swap places!

                swap(id, index)

            #swap all other values

                swap(age, index)
                swap(lname, index)
                swap(fname, index)
                swap(allegiance, index)

import csv

num_rec = 0
binary_code = 0
search_count = 0

id = []
fname = []
lname = []
allegiance = []
age = []

#with open("‪C:\\Users\\008006095\\Downloads\\GOT_bubble_sort_7.txt") as csvfile:
with open("C:\\Users\\008006095\\Downloads\\GOT_bubble_sort_7.txt") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:#process file data into lists

        id.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])

        num_rec += 1
answer = search_menu()#displaying menu
while True:#infinite loop
    
    while answer == 1:#option 1
        clear()
        fnamesort(fname)#sort by fname
        loop = "y"
        while loop == "y":
            clear()
            min = 0#setting min value for bianry search
            max = num_rec - 1#setting max value for binary search
            guess = int((min + max) / 2)#setting guess value for binary search
            search = input("Enter the First Name: ")
        
        
        
            while (min < max and search != fname[guess]):#setting loop that runs untill search term is foudn or thew whole file has been searched
                binary_code += 1
                if search < fname[guess]:
                    max = guess - 1#if the search value is less than the name at index value guess recalc max
                else:
                    min = guess + 1#if the search value is less than the name at index value guess recalc min
                guess = int((min + max) / 2)#recalculate middle value
            if search == fname[guess]:
                print("\n\nFIRST NAME:",search,"\nLAST NAME:",lname[guess],"\nAGE:",age[guess],"\nALLEGIANCE:",allegiance[guess],"\nID:", id[guess])
                print("Search Count:",binary_code)
            else:
                print("The person with the first name",search,"was not found.")
                print("Search Count:",binary_code)
            loop = doitagain()#continue searching
        clear()
        answer = search_menu()





    while answer == 2:#option 2
        clear()
        idsort(id)#sort by id
        loop = "y"
   
    
        while loop == "y":
            clear()
            min = 0#setting min value for bianry search
            max = num_rec - 1#setting max value for binary search
            guess = int((min + max) / 2)#setting guess value for binary search
            search = input("Enter the ID: ")
            while (min < max and search != id[guess]):#setting loop that runs untill search term is foudn or thew whole file has been searched
                binary_code += 1
                if search < id[guess]:
                    max = guess - 1#if the search value is less than the name at index value guess recalc max
                else:
                    min = guess + 1#if the search value is less than the name at index value guess recalc min
                guess = int((min + max) / 2)#recalculate middle value
            if search == id[guess]:
                print("\n\nFIRST NAME:",fname[guess],"\nLAST NAME:",lname[guess],"AGE:",age[guess],"ALLEGIANCE:",allegiance[guess],"ID:", search)
                print("Search Count:",binary_code)
            else:
                print("The person with the id",search,"was not found.")
                print("Search Count:",binary_code)
            loop = doitagain()
        clear()
        answer = search_menu()



    while answer == 3:#option 3 sequential search
        clear()
        loop = 'y'
        while loop == 'y':
            clear()

            search_last = input("What is the Last Name? ")

            found = -1
            last_length = len(lname)
            for n in range(0, last_length):
                if search_last == lname[n]:
                    found = n
                    print("\nPerson with last name {0} has Been Found\n\nID: {1:1} \nLast Name: {2:10} \nFirst Name: {3:10} \nAge: {4:10} \nAllegiance: {5:10}\n".format(search_last, id[found], lname[found], fname[found], age[found], allegiance[found]))
            if found < 0:
                print("Your Search for", search_last, "Was NOT FOUND")
                print("Check Your Spelling And Try Again")
            loop = doitagain()

        clear()
        answer = search_menu()



    while answer == 4:#option 4 sequential search
        clear()
        loop = 'y'
        while loop == 'y':
            clear()

            search_last = input("What is the Allegiance? ")

            found = -1
            last_length = len(allegiance)
            for n in range(0, last_length):
                if search_last == allegiance[n]:
                    found = n
                    print("\nPerson with allegiance {0} Has Been Found \n\nID: {1:1} \nLast Name: {2:10} \nFirst Name: {3:10} \nAge: {4:10} \nAllegiance: {5:10}\n\n".format(search_last, id[found], lname[found], fname[found], age[found], allegiance[found]))
            if found < 0:
                print("Your Search for", search_last, "Was NOT FOUND")
                print("Check Your Spelling And Try Again")
            loop = doitagain()
        clear()
        answer = search_menu()
    if answer == 5:#goodbye message
        goodbye()
        break