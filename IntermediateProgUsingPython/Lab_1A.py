#Lab1A Vignesh Peddi
answer = "y"
while answer == "y":
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
    answer = input("\n\nDo you want to check any more rooms[y/n]? ")
