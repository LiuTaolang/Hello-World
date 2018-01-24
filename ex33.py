def create_list():
    i = 0
    numbers = []
    get_num = int(input("Enter an integer: "))
    while i < get_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

numbers = create_list()

print("The numbers: ")

for num in numbers:
    print(num)
