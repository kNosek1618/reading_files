
#second information is 'mode'
#'r' - only read information
#'w' - can change information
#'a' - can append new informaction but can't change older
#'r+' - you have all the power in reading and writing
variable = open("files.txt", "r+")

print(variable.read())
variable.close()