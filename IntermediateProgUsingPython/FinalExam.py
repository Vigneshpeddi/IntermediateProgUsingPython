#Final Exam Vignesh Peddi 3/12/20 SE126CHS
#PROMPT: Process the list of students scores and allow an user to search the file
from os import system, name 
import csv
def goodbye():#goodbye function
    print("Goodbye")
def searchagain():#continue searching function that allows you to keep searching
    d = input("Would you like to search again[y/n]: ")
    while d != "Y" and d != "y" and d != "N" and d != "n":
        d = input("Would you like to search again[y/n]: ")
    return d
def swap(n, j):

    t = n[j]
    n[j]= n[j + 1]
    n[j + 1] = t
def average(x, y):
    averagescore = x / y
    return averagescore

#VARIABLE DICTIONARY
#averagetotal = 0    #the total sum of averages in the classroom
#binary_code = 0     #the number of searchs performed
#records = 0 #the number of records in the file
#test1 = []#test 1 score
#test2 = []#test 2 score
#test3 = []#test 3 score
#test4 = []#test 4 score
#test5 = []#test 5 score
#averager = []#averages of students
#name = []#names of students

#BASE PROGRAM
averagetotal = 0    #the total sum of averages in the classroom
binary_code = 0     #the number of searchs performed
records = 0 #the number of records in the file
test1 = []#test 1 score
test2 = []#test 2 score
test3 = []#test 3 score
test4 = []#test 4 score
test5 = []#test 5 score
averager = []#averages of students
name = []#names of students
print('{0:10} {1:5} {2:5} {3:5} {4:6} \t{5:6} \t{6:6}'.format('LASTNAME','TEST 1', 'TEST 2', 'TEST 3', 'TEST 4', 'TEST 5','AVERAGE'))
with open('Z:\\Finals\\final.txt') as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        records += 1
        name.append(rec[0])
        test1.append(int(rec[1]))
        test2.append(int(rec[2]))
        test3.append(int(rec[3]))
        test4.append(int(rec[4]))
        test5.append(int(rec[5]))
for i in range(0, records):
    averager.append(average((test1[i]+test2[i]+test3[i]+test4[i]+test5[i]), 5))
for i in range(0, records):
    print('{0:10} {1:5} {2:5} {3:5} {4:5} \t{5:5} \t{6:5.2f}'.format(name[i], test1[i], test2[i], test3[i], test4[i], test5[i], averager[i]))
for i in range(0, records):
    averagetotal += averager[i]
print("There are",records,"students in this classroom with an average of:",averagetotal/records)
answer = 'y'
while answer == 'y' or answer == 'Y':
    for i in range(0, records - 1):#outer loop

        for index in range(0, records - 1):#inner loop

            #below if statement determines the sort
            #list used is the list being sorted
            # > is for increasing order, < for decreasing
                if(name[index] > name[index + 1]):
                #if above is true, swap places!
                #temp = name[index]
                #name[index] = name[index + 1]
                #name[index + 1] = temp
                    swap(name, index)

                #swap all other values
                #temp = age[index]
                #age[index] = age[index + 1]
                #age[index + 1] = temp
                    swap(test1, index)
                    swap(test2, index)
                    swap(test3, index)
                    swap(test4, index)
                    swap(test5, index)
                    swap(averager, index)
    min = 0
    max = records - 1
    guess = int((min+max)/2)
    search = input("What is the last name: ")
    while (min < max and search != name[guess]):#setting loop that runs untill search term is foudn or thew whole file has been searched
        binary_code += 1
        if search < name[guess]:
            max = guess - 1#if the search value is less than the name at index value guess recalc max
        else:
            min = guess + 1#if the search value is less than the name at index value guess recalc min
        guess = int((min + max) / 2)#recalculate middle value
    if search == name[guess]:
        print('\nThe person with last name',search,"has been found with record: \nLASTNAME:",name[guess],"\nTEST 1:",test1[guess],"\nTEST 2:",test2[guess],"\nTEST 3:",test3[guess],"\nTEST 4:",test4[guess],"\nTEST 5:",test5[guess]," \nTEST 6:",averager[guess])
        print("Search Count:",binary_code)
    else:
        print("The person with last name",search,"has not been found")
        print("Search Count:",binary_code)
    answer = searchagain()
goodbye()