# Jack and his three friends have decided to go for a trip by sharing the expenses of the fuel equally.

# Write a Python program to calculate the amount (in Rs) each of them need to put in for the complete
# (both to and fro) journey.
# The program should also display True, if the amount to be paid by each person is divisible by 5,
# otherwise it should display False.
# (Hint: Use the relational operators in print statement.)

# Assume that mileage of the vehicle, amount per litre of fuel and distance for one way are given.

mileage = 12
amount_per_litre = 65
distance_one_way = 96
per_head_cost = 0
divisible_by_five = False
total_fuel_used = distance_one_way/mileage
total_cost = total_fuel_used*amount_per_litre
if((total_cost/2) % 5 != 0):
    divisible_by_five = False
else:
    divisible_by_five = True
per_head_cost = total_cost/4
print(per_head_cost)
print(divisible_by_five)
