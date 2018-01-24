cars = 100           # the totality of cars
space_in_a_car = 4.0 # using 4.0 for variable space_in_a_car shows that it's a float point number. the capacity of a car.
drivers = 30         # the totality of drivers
passengers = 90      # the totality of passengers
cars_not_driven = cars - drivers  # the totality of not driven cars
cars_driven = drivers             # the totality of driven cars
carpool_capacity = cars_driven * space_in_a_car    # the capacity of all driven cars
average_passengers_per_car = passengers / cars_driven # the number of passengers in one car


print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
