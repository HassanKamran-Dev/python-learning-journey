#Search word in a file and print how many time it appears
with open("search.txt","r") as file:
    content = file.read()
    words = content.split()
    word = "Fahad"
    number_of_times = words.count(word)
    print(f"{word} appears {number_of_times} times!")

#To Replace one word with other
with open("search.txt","r+") as file:
    content = file.read()
    file.seek(0)
    file.write(content.replace("Fahad","Shehroz"))
    
