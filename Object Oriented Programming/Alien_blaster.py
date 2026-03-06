class Player(object):
    def blast(self,enemy):
        print("The player blast an enemy.\n")
        enemy.die()

class Alien(object):
    def die(self):
        print("The alien gasps and says, 'Oh, this is it Good-bye!\n")

def main():
    print("\t\tDeath of an Alien\n")

    hero = Player()
    invader = Alien()
    hero.blast(invader)

if __name__ == "__main__":
    main()