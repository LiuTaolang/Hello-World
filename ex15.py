from sys import argv                      # import the 'argv' module from sys

script, filename = argv                   # unpack the argv. first parameter is the script's name, secondary and after,if argv has, will input by user
                                          # here use argv to get text file name. user only input one argument before the script runs.
txt = open(filename)                      # open(filename) means the file will be opened by read-only, which is default.

print(f"Here's your file {filename}:")    # print a little information
print(txt.read())                         # .read() function is to get text from txt and then print.

print("Type the filename again:")         # give a prompt to user
file_again = input("> ")                  # get a filename through keyboard by user.

txt_again = open(file_again)              # get text from the txt.

print(txt_again.read())                   # print that.
