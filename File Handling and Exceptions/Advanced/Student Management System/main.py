class Student:
    def __init__(self,name="",rollnum=0,cgpa=0):
        self.name = name
        self.rollnum = rollnum
        self.cgpa = cgpa
    
    def add_student(self):
        try:
            filename="data.txt"
            with open(filename,'a') as file:
                self.name = input("Enter Name (To Add): ")
                self.rollnum = int(input("Enter Roll number: "))
                self.cgpa = input("Enter CGPA: ")
                file.write(f"\n{self.name} {self.rollnum} {self.cgpa}")
        except Exception as e:
            print(f"Sorry an unexpected error occured {e}")

    def view_students(self):
        try:
            filename="data.txt"
            with open(filename,'r') as file:
                students = file.read()
                print("Students: ")
                print(students)
        except FileNotFoundError:
            print(f"File {filename} does not found!")
    
    def search_student(self):
        try:
            filename="data.txt"
            with open(filename,'r') as file:
                search_roll = int(input("Enter Roll number (To Search): "))
                found = False
                for line in file:
                    parts = line.split()
                    if len(parts) < 3:
                        continue
                    name = parts[0]
                    rollnumber = int(parts[1]) 
                    cgpa = parts[2] 
                    if search_roll == rollnumber:
                        print("Student found!")
                        print("Data: ")
                        print(f"\t{name} {rollnumber} {cgpa}")
                        found = True
                        break
                if not found:
                    print("Student not found!")
        except FileNotFoundError:
            print(f"File {filename} does not found!")

if __name__ == '__main__':
    s1 = Student()
    s2 = Student()
    s3 = Student()

    #s1.add_student()
    #s2.add_student()
    #s3.add_student()

    #s1.view_students()

    s1.search_student()





                                    
            

