class User:
    def __init__(self,username,salary,email):
        self.name = username
        self.sal = salary
        self.mail = email
        self.attempts = 0

    def describe_user(self):
        print(f"Username: {self.name}, Salary: {self.sal}, Email: {self.mail}")
        
    def increment_login(self):
        self.attempts+=1

    def reset_login(self):
        self.attempts=0

    def print_attempts(self):
        print(f"Attempts: {self.attempts}")

class Privileges:
    def __init__(self,privileges=None):
        if privileges == None:
            self.priv = []
        else:
            self.priv = privileges

    def show_priv(self):
        for i in self.priv:
            print(f"Admin {i}")
    

class Admin(User):
    def __init__(self, username, salary, email):
        super().__init__(username, salary, email)
        self.privileges = Privileges(["can add img","can delete user","can make a post"])



u1 = User("Hassan",200,"h111")
u2 = User("Azeem",500,"A2323")
u3 = User("Nouman",700,"N33")

#u2.describe_user()
#u3.describe_user()

#u1.increment_login()
#u1.increment_login()
#u1.increment_login()
#u1.print_attempts()

#print("Resetting the attempts")
#u1.reset_login()
#u1.print_attempts()

#ad1 = Admin("Hassan",200,"h111")
#ad2 = Admin("Azeem",624,"A111")

#ad2.privileges.show_priv()



   
