'''
The logging module is included with the Python standard library.
It contains functions and classes for creating a logging system 
for software applications.
* default logging level is "warning". 
* we can change the default configuration with the logging module's 
basicConfig() function. 
* Syntax is debug(msg, *args, **kwargs). same syntax applicable for
    info, warning, error and critical  
'''
import logging

# setting the logging level to DEBUG. The default level is Warning
# and above.
# logging.basicConfig(level=logging.DEBUG)
# Specify the log file, format of message and logging level.
logging.basicConfig(filename = "/Users/kader8/learning/python_basics/07_logging_error_handling/example.log", 
                    format="%(asctime)s %(levelname)s %(message)s",
                    level=logging.INFO)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("Application faced a error situation")
logging.critical("P1 critical error")

#separator block 
print("-" * 50)

# Example of logging in a function.
def add_numbers(x, y):
    ''' Add two numbers and provide result '''
    # check if arguments are not of number type, then log a warning
    if (type(x) != type(y)):
        logging.warning("Args may not be compatible")
    # check if arguments are of string, then log a error.
    if ( type(x) == str and type(y) == str):
        logging.error("Result is concatenated string")
    # check if they are of bool or str type.
    if (type(x) != type(y)) and (type(x) in (bool, str) or type(y) in (bool, str)):
        logging.critical("result cannot be processed")
        return ""

    logging.debug(f"x = {x} and y = {y}")
    logging.info(f"function returns : {x+y}")
    return x+y

def main():
    add_numbers(2, 3)


'''
Below example of logging to the file. The syntax is as follows:
logging.basicconfig(filename:<"path of file">), 
                    format = "%(asctime)s %(levelname)s %(message)s",
                    level = logging.<level>)
'''
# Challenge: Using the logging module
# 1. Write log messages to a file named example.log.
    # mlog message should include the time it 
    # was logged, the level name, and a message. 
    # All logs at level INFO and higher should be logged


# method that will check and do the following
#   1. receive user input of numbers as comma separated values.
#   2. validate if there is comma, if not log error that says "Try again"
#   3. convert to integer list and return list.
#   4. Add INFO level logging to indicate the following in method
#           a. Start of method.
#           b. report number of items entered.
#           c. final info to return the list of integers.
def process_data():
    #Separator block
    print("-" * 50)
    logging.info("Function started")

    # receive raw input of comma separated values
    raw_data = input("Enter a series of numbers as comma separated : ")
    
    # check if the raw_data string contains comma
    if ("," not in raw_data):
        logging.error("User did not enter comma separated values")
        logging.info("function returns 'Try again'")
        return "Try again"
    
    # Strip the comma and populate the values to list
    str_list = raw_data.split(",")
    logging.info("user input is %i items long", len(str_list))

    # Convert them in to integer list using list comprehension
    num_list = [int(x) for x in str_list]
    logging.info("function returns %s ", num_list)
    #return the converted list
    return (num_list)

if __name__ == '__main__':
    main()
    process_data()

