cars = 4
trucks = 2
people = int(input('How many people in all?'))

if people < 16:
    print("We should take the cars.")
elif people < 20:
    print("We should not take the cars.")
else:
    print("We can't decide.")
"""
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We stll can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
"""
