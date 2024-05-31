'''
open(<file_name>, <mode>) will be the method used on a file
<mode>
x - create [Creates a file]
w - write [Writes into a file]
    if file doesnt exist
        creates
    else
        overwrites.
a - appends to an existing file.
r -  Default value and reads the entire file. 
'''
import os

# Open file with "w" command. This will create the file.
f = open("welcome.txt" , "w")
# Write to the file.
f.write("Hello, welcome to Python file writing module")
# close the stream.
f.close()

# read the file.
f = open("welcome.txt", "r")
print(f.read())
f.close()

#append data to existing welcome.txt file.
f = open("welcome.txt", "a")
f.write("Example for append call")
f.close()
# read the file.
f = open("welcome.txt", "r")
print(f.read())
f.close()

# read the first 5 bytes of file.
f = open("welcome.txt", "r")
print(f.read(5))
f.close()

#delete the file
if (os.path.exists("welcome.txt")):
    os.remove("welcome.txt")
    print("welcome.txt deleted")
else:
    print("welcome.txt does not exits")