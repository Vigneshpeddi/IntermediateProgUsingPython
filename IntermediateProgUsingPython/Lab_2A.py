#Lab 2A Vignesh Peddi
import csv
tr = 0
over_rec = 0
print("{0:37} {1:20} {2:20} {3:20}".format("Room", "Max", "Attending", "Over"))
with open("C:/Users/008006095/Downloads/lab2a.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        tr += 1
        room_name = rec[0]
        room_capacity = int(rec[1])
        attendees = int(rec[2])
        if attendees >= room_capacity:
             over = attendees - room_capacity
             over_rec += 1
             print("{0:20} {1:20} {2:20} {3:20}".format(room_name, room_capacity, attendees, over))
        else:
            over = 0
        
       

print("Processed",tr,"records")
print("There are",over_rec,"rooms over the limit.")

    