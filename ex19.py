def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

'''
study drills 3, write at least one more function of your own design, and run it 10 different ways.
'''
def IU(song_name):       #  print a song's name of IU
    print(f"IU is a singer from South Korea. I love her song {song_name} very much.")

print("Print default song's name first.")
IU('U&I')

song_name = input("Tell me which IU's song is your favorite: ")
IU(song_name)
