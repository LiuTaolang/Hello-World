from sys import argv

script, input_file = argv                      # load the module argv from sys.

def print_all(f):
    print(f.read())                            # call .read() method

def rewind(f):
    f.seek(0)                                  # move to the start of the file.

def print_a_line(line_count, f):
    print(line_count, f.readline())            # call .readline() method, read just one line of the content

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
