class Critter(object):
    def __init__(self,name,hunger = 0,boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def __str__(self):
        print(f"Name: {self.name} | Hunger:{self.hunger} | Boredom: {self.boredom}")
        return ""
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    
    @property
    def mood(self):
        unhappiness = self.boredom + self.hunger
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")  
        self.__pass_time()

    def eat(self,food=4):
        print("Brrupp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger=0
        self.__pass_time()

    def play(self,fun=4):
        print("Wheeee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
         Critter Caretaker

         0 - Quit
         1 - Listen to your critter
         2 - Feed your critter
         3 - Play with your critter   
        """)
        choice = input("Choice: ")
        print()
        if choice == "0":
            print("Good-bye!")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            food_quantity = int(input("How much food you want to give? : "))
            crit.eat(food_quantity)
        elif choice == "3":
            time = int(input("How much time do you want to play : "))
            crit.play(time)
        elif choice == "4":
            print(crit)    
        else:
            print(f"Sorry but {choice} is not a valid choice.")
        
if __name__ == "__main__":
    main()