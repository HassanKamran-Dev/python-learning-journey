fathernames = {
    "Hassan": "Kamran",
    "Nouman": "Tariq",
    "Azeem": "Tahir",
    "Shehroz" : "Ahmed"
}

choice = None

while choice != "0":
    print(
    """
    Who is Your Daddy Program
        0 - Quit
        1 - Ask
        2 - Add 
        3 - Replace
        4 - Delete
    """)
    choice = input("Enter your choice: ")
    if choice == "0":
        print("Goodbye!")
    elif choice == "1":
        name = input("Enter Name (To Ask): ")
        if name in fathernames:
            print(f"Your Dad name is {fathernames[name]}")
        else:
            print("Sorry i don't know this person")
    elif choice == "2":
        name = input("Enter Name (To Add): ")
        if name not in fathernames:
            fathername = input("Enter Dad Name: ")
            fathernames[name]=fathername
            print("Information Added!")
        else:
            print("This person already exist in dictionary")
    elif choice == "3":
        name = input("Enter Name (To Replace): ")
        if name in fathernames:
            repname = input("Enter Name (To Replace with): ")
            fathernames[name]=fathernames[repname]
            print("Both Dad is replaced!")
        else:
            print("Sorry i don't know this person")
    elif choice == "4":
        name = input("Enter Name (To Delete): ")
        if name in fathernames:
            del fathernames[name]
            print("Information Deleted!")
        else:
            print("Sorry i don't know this person")

