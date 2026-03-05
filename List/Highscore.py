scores = []

choice = None

while choice != "0":
    print("\n----High Scores---- \n" 
    "0 - Exit\n" 
    "1 - Show Scores\n" 
    "2 - Add a Score\n" 
    "3 - Delete a Score\n" 
    "4 - Sort Scores")
    choice = input("Choice: ")

    if choice == "0":
        print("Good bye!")
    elif choice == "1":
        print("High Scores: ")
        for score in scores:
            print(score)
    elif choice == "2":
        score = int(input("What score did you get? "))
        scores.append(score)
    elif choice == "3":
        score = int(input("What score you want to remove? "))
        if score in scores:
            scores.remove(score)
        else:
            print(score,"Is'nt in the score list")
    elif choice=="4":
        scores.sort(reverse=True)

