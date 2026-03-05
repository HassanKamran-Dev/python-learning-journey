import json



def alr_stored():
    filename = "favourite.json"
    try:
        with open(filename,"r") as f_obj:
            number = json.load(f_obj)
    except:
        pass
    else:
        return number
        
def get_number():
    favNumber = alr_stored()
    if favNumber:
        print("You'r favourite number is:",favNumber)
    else:
        favNumber = input("What's your favourite number? :")
        filename = "favourite.json"
        with open(filename,"w") as f_obj:
            json.dump(favNumber,f_obj)

get_number()
