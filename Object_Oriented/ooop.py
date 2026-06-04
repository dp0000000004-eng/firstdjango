class Faculty:
    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.age = int(input("Enter Your Age: "))
        self.salary = int(input("Enter salary: "))
    def __str__(self):
        return f"""Name Of Employee: {self.name}
Age Of Employee:  {self.age}
Salary Of Employee:  {self.salary}"""

f = Faculty()
print(f)