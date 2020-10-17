#Vignesh Peddi Lab 2B
import csv
print("{0:10} {1:10} {2:10} {3:10} {4:10} {5:8} {6:10} {7:6} {8:5} ".format("Type", "Brand", "CPU", "Ram", "1st Disk", "No. HDD", "2nd Disk", "OS", "YR"))#Fformat the labels
with open("C:/Users/008006095/Downloads/lab2b.csv") as csvfile:#open csv
    file = csv.reader(csvfile)#read csv
    for rec in file:#creating loop
        type = rec[0]#setting type to record 0
        if type == 'D':
            type = "Desktop"#changing type - desktop if d
        elif type == "L":
            type = "Laptop"#changing type to laptop if type is l
        brand = rec[1]#setting brand
        if brand == "D":#changing brand to full name
            brand = "Dell"
        if brand == "HP":
            brand = "HP"
        if brand == "GW":
            brand = "Gateway"
        processor = rec[2]#setting processor to rec 2
        ram = rec[3]#setting ram to rec 3
        hdd_size = rec[4]#setting hdd_size to rec 4
        no_hdd = int(rec[5])
        if no_hdd == 1:#set variables based on no of hdd
            os = rec[6]
            hdd2_size = " "
            year_pur = rec[7]
        if no_hdd == 2:
            hdd2_size = rec[6]
            os = rec[7]
            year_pur = rec[8]
        print("{0:10} {1:10} {2:10} {3:10} {4:10} {5:3} \t{6:10} {7:6} {8:4} ".format(type, brand, processor, ram, hdd_size, no_hdd, hdd2_size, os, year_pur))#print 
        
   
 
