class Employee:
    #Class variable
    employee_count = 0

    # constructor method
    def __init__(self, name, email, hire_date):
        #setting current object attributes
        self.name = name
        self.email = email
        self.hire_date = hire_date

        #incrementing class level variable.
        Employee.employee_count += 1

        #List to hold the posts
        self.posts = []
    
    def post_content(self, content):
        self.posts.append(content)


# create a instance of class Employee
e1 = Employee("Dilawar", "shahdilawar@gmail.com", "09/13/2021")
e1.post_content("Looking forward to the jon")
e1.post_content("Good onboarding experience!!!")

print(e1.name)
print(e1.email)
print(e1.hire_date)
print(e1.employee_count)
print(e1.posts)


# create another instance of class Employee
e2 = Employee("Parveen", "anoshaparveen@gmail.com", "06/15/2025")
print(e2.name)
print(e2.email)
print(e2.hire_date)
print(e2.employee_count)

'''
Create a Bank account class. Be sure to build the logic so that users 
cannot withdraw more money than they have in the account. Each bank account 
should have the following attributes and methods.
* A unique account number — this can be assigned sequentially.
* A balance instantiated with an opening deposit.
* A method for depositing money.
* A method for withdrawing money.
* A method that prints the account balance.
'''
class BankAccount:

    number_of_accounts = 0
    # Constructor method
    # Initializing account number and deposit.
    def __init__(self, deposit):
        account_number = BankAccount.number_of_accounts + 1
        self.account_number = str(account_number)
        self.balance = deposit
        # increment for the next account
        BankAccount.number_of_accounts += 1

    # method to accept deposit
    def deposit(self, deposit):
        self.balance += deposit

    # Method to withdraw. Check if withdraw amount is lesser
    # than available balance.
    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.balance:
            self.balance -= withdraw_amount
        else:
            print("Insufficient balance") 
    
    # Print available balance
    def get_balance(self):
        print(f"Balance is : {self.balance}")

bankAccount = BankAccount(50000)
bankAccount.deposit(25000)
bankAccount.withdraw(10000)
bankAccount.get_balance()



