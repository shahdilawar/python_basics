class Employee:
    # class attribute to track current number of employees
    employee_count = 0
    
    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email and hire date. 
        Adjusts the employee_count class attribute when a new employee 
        is created. 
        """
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        # Initialize an empty array
        self.posts = []
        # Initializes an empty list to hold all comments
        self.comments = []

    # Employee object toString method.
    def __str__(self):
        return f"Employee : {self.name} \nHire Date : {self.hire_date}"

# Create sub classes of Employee of type Engineer
class Engineer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "engineering"
    
    def __str__(self):
        super_obj_str =  super().__str__()
        return f"{super_obj_str} \ndepartment : {self.department}"

# Create sub classes of Employee of type Marketer
class Marketer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "marketing"

    def __str__(self):
        super_obj_str =  super().__str__()
        return f"{super_obj_str} \ndepartment : {self.department}"


eng1 = Engineer("Aashik", "aashik@gmail.com", "07/20/2022")
mar1 = Marketer("Anosha", "anosha@gmail.com", "06/15/2022")
print(eng1)
print(mar1)
print(Employee.employee_count)