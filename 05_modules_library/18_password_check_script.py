from Password_Checker import password_strength_check
'''
Script to check password strength.
Import the Password_Checker module and use password_strength_check
funtion
'''


#Define a function to receive user input and test on strength
# and communicate if its good.
def password_check():
    password_strength = False
    while (password_strength == False):
        password_string = input("Please enter a pasword : ")
        #call the password strength function from the imported module
        # and store the strength returned into the score variable
        score = password_strength_check(password_string)

        if (score < 3):
            print(f" password score : {score}, It is weak try again")
        elif (score <= 4):
            print(f" password score : {score}, It is moderate and accepted")
            password_strength = True
        elif (score > 4):
           print(f" password score : {score}, It is strong and accepted")
           password_strength = True

if (__name__ == '__main__'):
    password_check()