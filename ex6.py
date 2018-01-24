types_of_people = 10                                  # a variable means 10 types of people
x = f"There are {types_of_people} types of people."   # a variable contains a sequence of string

binary = "binary"                                     # a variable with evaluation of string
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #a variable contains a sequence of string, f-string

print(x)                                              # print the string in x
print(y)                                              # print the string in y

print(f"I said: {x}")                                 # print the "I said:" + x by "f-string"
print(f"I also said: '{y}'")                          # print the "I also said:" + 'y' by "f-string"

hilarious = False                                     # a boolean variable with evaluation False
joke_evaluation = "Isn't that joke so funny?! {}"     # a variable with evaluation of string

print(joke_evaluation.format(hilarious))              # use "format" to transfer hilarious's value to {} in joke_evaluation

w = "This is the left side of..."                     # a variable with evaluation of string
e = "a string with a right side."                     # ditto

print(w + e)                                          # join string of w and e then print
