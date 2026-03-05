#To print number of words
with open("read.txt","r") as file:
        context = file.read()
        words = context.split()
        print(f"Number of words: {len(words)}")

#To print number of characters
with open("read.txt","r") as file:
    context = file.read()
    print(f"Number of characters: {len(context)}")

#To print number of lines
with open("read.txt","r") as file:
    context = file.readlines()
    print(f"Number of lines: {len(context)}")

#To append new text to an existing file without deleting old data
with open("read.txt","a") as file:
     file.write("\nFahad Mehmood")

#To copy content from one file to another
with open("read.txt","r") as file1, open("write.txt","w") as file2:
    content = file1.read()
    file2.write(content)
    print(f"Successfully copied!")
     
    

    





