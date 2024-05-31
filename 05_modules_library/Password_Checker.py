'''  
module that includes functions that check a string for complexity, and return a password strength
score to the user.
* Add a function to check if it contains Number
* Add a function to check if it contains Upper case
* Add a function to check if it contains lower case
* Add a function to check if it contains special character
'''
#Define the string that contains all the special characters
special_characters = "`~!@#$%^&*()_-+={}[]:;\"'\"<,>.?/"

#Define a function to check if it contains number
def contains_number(password_string):
    #Iterate through each character in password string
    for char in password_string:
        #Check if password string contains numberic values
        if (char.isnumeric()):
            return True
    return False

#Define a function to check if it contains upper case
def contains_upper_case(password_string):
    #Iterate through each character in password string
    for char in password_string:
        #check if password string contains upper case
        if (char.isupper()):
            return True
    return False

#Define a condition to check if it contains lower case
def contains_lower_case(password_string):
    #Iterate through each character in password string
    for char in password_string:
        #check if password string contains lower case
        if (char.islower()):
            return True
    return False

#Define a condition to check if it contains special case characters
def contains_special_characters(password_string):
    for char in password_string:
        #check if password string contains special characters.
        if (char in special_characters):
            return True
    return False

# Password strength calculator function that calls the above 
# functions to calculate and return the strength score of the 
# given password string.
def password_strength_check(password_string):

    password_score = 0
    if (contains_number(password_string)):
        password_score += 1
    if (contains_upper_case(password_string)):
        password_score +=1
    if (contains_lower_case(password_string)):
        password_score += 1
    if (contains_special_characters(password_string)):
        password_score += 1
    if (len(password_string) > 8 ):
        password_score += 1

    return password_score


