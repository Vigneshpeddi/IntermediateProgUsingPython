#Lab 4A Vignesh Peddi
#STARTING DOCUMENTATION
#PROMPT: •	Process the lists to print the them as they appear in the file
#•	Re-process the lists to add the House Motto (dependent on Field4/Allegiance)
#o	Re-Process the lists to print each record fully with the House Mottos
#•	Re-process the lists to find the average age within the list, then
#o	Print the total number of people in the list
#o	Print the average age
#o	Print tallies for each allegiance (Field4)
#VARIABLE DICTIONARY
#a_tally_hs       tallies for everyone in House Stark
#a_tally_hb       tallies for everyone in House Baratheon
#a_tally_ht       tallies for everyone in House Tully
#a_tally_nw       tallies for everyone in Night's Watch
#a_tally_hl       tallies for everyone in House Lannister
#a_tally_hta      tallies for everyone in House Stark
#t_age            total age
#tr               total records
#fname            LIST stores the first names
#lname            LIST stores the last names
#age              LIST stores the ages
#nickname         LIST stores the nicknames
#allegiance       LIST stores the allegiances
#motto            LIST stores the mottos
#BASE PROGRAM
import csv
print("{0:15} {1:15} {2:5} {3:20} {4:30} {5:5}".format("First Name", "Last Name", "Age", "Nickname", "House Allegiance", "House Motto"))
a_tally_hs = 0
a_tally_hb = 0
a_tally_ht = 0
a_tally_nw = 0
a_tally_hl = 0
a_tally_hta = 0
t_age = 0
tr =  0
fname = []
lname = []
age = []
nickname = []
allegiance = []
motto = []
with open("D:/Downloads/lab4A_GOT_NEW.txt") as csvfile:
  file = csv.reader(csvfile)
  for rec in file:#storing data into lists
    fname.append(rec[0])
    lname.append(rec[1])
    age.append(int(rec[2]))
    nickname.append(rec[3])
    allegiance.append(rec[4])
    tr+=1

  for i in range(0, tr):#counting the records in the file
      t_age += age[i]

  for i in range(0, tr):#adding mottos ad tallies for houses
    if allegiance[i] == "House Stark":
      a_tally_hs += 1
      motto.append("Winter is Coming")
    if allegiance[i] == "House Baratheon":
      a_tally_hb += 1
      motto.append("Ours is the fury.")
    if allegiance[i] == "House Tully":
      a_tally_ht += 1
      motto.append("Family.Duty.Honor")
    if allegiance[i] == "Night's Watch":
      a_tally_nw += 1
      motto.append("And now my watch begins.")
    if allegiance[i] == "House Lannister":
      a_tally_hl += 1
      motto.append("Hear me Roar!")
    if allegiance[i] == "House Targaryen":
      a_tally_hta += 1
      motto.append("Fire & Blood")
    print("{0:15} {1:13} {2:4} \t{3:20} {4:25} {5:10}".format(fname[i], lname[i], age[i], nickname[i], allegiance[i], motto[i]))
  avg_age = t_age/tr#calculate avg age
  #print values
  print("\nThere are",tr,"people in this list!")
  print("The average age is {0:.0f} years!".format(avg_age))
  print("\nTallies")
  print("House Stark:",a_tally_hs)
  print("House Baratheon:",a_tally_hb)
  print("House Tully:",a_tally_ht)
  print("Night's Watch:",a_tally_nw)
  print("House Lannister:",a_tally_hl)
  print("House Targarayen:",a_tally_hta)
  

  



