def student_process_data(filename):
    highest_scorers = []
    max_marks = -1
    highest_scorer = None

    try:
        with open(filename,'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) < 2:
                    continue
                name = parts[0]
                marks = int(parts[1])
                if marks > 80:
                    highest_scorers.append(name)
                if marks > max_marks:
                    max_marks = marks
                    highest_scorer = name
            print('Students who scored above 80: ')
            for student in highest_scorers:
                print(f"- {student}")
    except FileNotFoundError:
        print(f"File {filename} does not found.")
    
if __name__ == '__main__':
    student_process_data("students.txt")
