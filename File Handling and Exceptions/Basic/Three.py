#To Find Sum, Avg, Max and Min
numbers=[]
with open("numbers.txt","r") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:
            number = int(clean_line)
            numbers.append(number)
        
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"Total: {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")



