#Vignesh Peddi Lab 1
def capacity(rc):
    rc = int(input("What is the capacity of the room? "))
    return rc
def attendees(at):
    at = int(input("\nHow many people are attending? "))
    return at
def register(hmm):
    hmm = room_capacity - attendees1
    print('\n',hmm,'people can attend.')
def accept_or_not(a):
    a = input("Do you want to check anymore rooms?[y/n] ")
    if a != "n" and a != "N" and a != "Y" and a != "y":
        a = input("Do you want to check any more rooms?[y/n] ")
    return a

room_capacity = 0
attendees1 = 0
how_many_more = 0
answer = 'y'
while answer == "y" or answer == "Y":
    room_capacity = capacity(room_capacity)
    attendees1 = attendees(attendees1)
    how_many_more = register(how_many_more)
    answer = accept_or_not(answer)
    
      
