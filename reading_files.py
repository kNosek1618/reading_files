
#second information is 'mode'
#'r' - only read information
#'w' - can change information
#'a' - can append new informaction but can't change older
#'r+' - you have all the power in reading and writing
variable = open("files.txt", "r")

#read - read all files txt
print(variable.read())
#readline - read first line
#print(variable.readline())
#readline from index
#print(variable.readlines()[3])

variable.close()