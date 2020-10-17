 #LAB 3B Vignesh Peddi


#PROGRAM PROMPT:
#3B Construct a program that will analyze potential voters. The program should generate the following totals:

#1.	Number of males not eligible to register.
#2.	Number of females not eligible to register.
#3.	Number of males who are old enough to vote but have not registered.
#4.	Number of females who are old enough to vote but have not registered.
#5.	Number of individuals who are eligible to vote but did not vote.
#6.	Number of individuals who did vote.
#7.	Number of records processed.

#The program must prompt the user for the ID number, age, gender, if the person is registered to vote, and if the person voted.  You will also have to prompt to see if the user has more data to enter. 



#ID Number is 4 characters
#   Age is a number
#   Gender is either an F or an M
#   Registered is either an N or a Y
#   Votes is either an N or a Y

#VARIABLE DICITONARY
#id_num         LIST  id number
#age            LIST  age
#gen            LIST  gender
#reg            LIST  response to being regisered or not
#vote           LIST  response to voting
#male2young     Number of males not eligible to register.
#female2young   Number of females not eligible to register.
#male_noReg     Number of males who are old enough to vote but have not registered.
#female_noReg   Number of females who are old enough to vote but have not registered.
#novote         Number of individuals who are eligible to vote but did not vote.
#total_vote     Number of individuals who did vote.
#records        Number of records processed.


#PROGRAM START---------------------------------------------------------------------------

#initialize all variables that will be counting users (final 7 outputs)
import csv


male2young = 0 
female2young = 0 
male_noReg = 0
female_noReg = 0
novote = 0
total_vote = 0
records = 0
id_num = []
age = []
gen = []
reg = []
vote = []
#with open("‪‪‪C:/Users/008006095/Desktop/voters_new.csv") as csvfile:
with open("C:/Users/008006095/Desktop/voters_new.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for rec in file:

        id_num.append(int(rec[0]))
        age.append(int(rec[1]))
        gen.append(rec[2])
        reg.append(rec[3])
        vote.append(rec[4])

    #7.	Number of records processed.
        records += 1               #output #7
    for index in range(0,records):

    #1.	Number of males not eligible to register.
        if gen[index] == "M":        #checks for male response

            if age[index] < 18:                  #checks that user is too young to register

            #this process does not run unless preceding if statements (Where this process is nested) are both TRUE
                male2young += 1 

            #print(male2young) #for testing, commented out when program was finished


    #2.	Number of females not eligible to register.
        if gen[index] == "F":        #checks for female response

            if age[index] < 18:                  #checks that user is too young to register

            #this process does not run unless preceding if statements (Where this process is nested) are both TRUE
                female2young += 1 

            #print(female2young) #for testing, commented out when program was finished


    #3.	Number of males who are old enough to vote but have not registered.
        if gen[index] == "M":        #checks for male response

            if age[index] >= 18:                 #checks if user is old enough to be eligible to vote

                if reg[index] == "n" or reg[index] == "N":#checks that they are not registered

                #this process does not run unless preceding if statements (Where this process is nested) are all TRUE
                    male_noReg += 1

                #print(male_noReg) #for testing, commented out when program was finished

    #4.	Number of females who are old enough to vote but have not registered.
        if gen[index] == "F":        #checks for female response

            if age[index] >= 18:                 #checks for age eligibility

                if reg[index] == "N":#checks registered response
                
                #this process does not run unless preceding if statements (Where this process is nested) are all TRUE
                    female_noReg = female_noReg + 1

                #print(female_noReg) #for testing, commented out when program was finished


    #5.	Number of individuals who are eligible to vote but did not vote.
        if reg[index] == "Y":        #checks registered response

            if age[index] >= 18:                 #checks for valid age

                if vote[index] == "N":#checks vote respone
            
                #this process does not run unless preceding if statements (Where this process is nested) are all TRUE
                    novote = novote + 1

                #print(novote) #for testing, commented out when program was finished

    #6.	Number of individuals who did vote.
        if reg[index] == "Y":        #checks registered response

            if age[index] >= 18:                 #checks for valid age

                if vote[index] == "Y":#checks vote respone
            
                #this process does not run unless preceding if statements (Where this process is nested) are all TRUE
                    total_vote = total_vote + 1

                #print(total_vote) #for testing, commented out when program was finished











    print("Number of males not eligible to register: ", male2young)
    print("Number of females not eligible to register: ", female2young)
    print("Number of males who are old enough to vote but have not registered: ", male_noReg)
    print("Number of females who are old enough to vote but have not registered:", female_noReg)
    print("Number of individuals who are eligible to vote but did not vote: ", novote)
    print("Number of individuals who did vote: ", total_vote)
    print("Number of records processed: ", records)

