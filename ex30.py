'''
people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
'''
cars = 4
trucks = 2
people = int(input('How many people in all?'))

if 2 <= people < 4 * cars:
    print("We should take the cars.")
elif 4 * cars <= people < 40 * trucks:
    print("We should not take the cars. Maybe trucks are better choice.")
elif people < 2:
    print("You single dog, just stay home!")
else:
    print("You may take the train.")
