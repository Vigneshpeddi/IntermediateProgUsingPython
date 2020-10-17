#Vignesh Peddi Lab 1B
answer = 'y'
while answer == "y" or answer == "Y":
    room_capacity = int(input("What is the capacity of the room? "))
    attendees = int(input("\nHow many people are attending? "))
    if attendees <= room_capacity:
        how_many_more = room_capacity - attendees
        print('\n\nYou meet fire regulations.', how_many_more,
              'more people can attend.')
    elif attendees >= room_capacity:
        how_many_less = attendees - room_capacity
        print("\n\nSorry, you don't meet fire regulations.", how_many_less,
              "people can't attend.")
    sparky = input("Do you want to check anymore rooms? ")
    if sparky == 'n':
        answer = 'n'
    while sparky != 'y' and sparky != 'Y' and sparky != 'N' and sparky != 'n':
        sparky = input("Do you want to check anymore rooms? ")
        if sparky == 'n' or sparky == 'N':
            answer = 'n'
            



   