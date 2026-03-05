attributes = {
    "Strength":0,
    "Health":0,
    "Wisdom":0,
    "Dexterity":0
    }

pool = 30

choice = None
while choice != "0":
    print(
    """ Welcome To Character Creator
        0 - Quit
        1 - Spend on Attributes
        2 - Take from Attributes
    """)
    choice = input("Enter choice: ")
    if choice == "0":
        print("Goodbye!")
    elif choice == "1":
        util = input("Name of Attribute (To SPEND POINTS): ")
        if util in attributes:
            points = int(input("How much you want to spend on it? "))
            attributes[util] = points
            pool-=points
            print(f"You have spent {points} on {util}")
            print(f"You have {pool} points now")
        else:
            print("Sorry this attribute does'nt exist")
    elif choice == "2":
        util = input("Name of Attribute (TO TAKE POINTS): ")
        if util in attributes:
            points = int(input("How much you want to take from it? "))
            if points < attributes[util]:
                attributes[util] = points
                pool+=points
                print(f"You have taken {points} from {util}")
                print(f"You have {pool} points now")
            else:
                print(f"Sorry {util} have {attributes[util]} points")
        else:
            print("Sorry this attribute does'nt exist")
    else:
        print("Enter a valid choice")
