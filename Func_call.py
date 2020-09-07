def display1(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)


print("code-1: positional arguments")
display1("AI789", 200)
# Uncomment and execute the below function call statement and observe the output
# display1(300,"BA123")


def display2(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)


print("-------------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="AI789")


def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)


print("-------------------------------------------------")
print("code-3: default arguments")
display3("AI789", "Eagle")
# Uncomment and execute the below function call statements one by one and observe the output
# display3("BA234")
# display3("SI678","Qantas",200)


def display4(passenger_name, *baggage_tuple):
    print("Passenger name:", passenger_name)
    total_wt = 0
    for baggage_wt in baggage_tuple:
        total_wt += baggage_wt
    print("Total baggage weight in kg:", total_wt)


print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack", 12, 8, 5)
# Uncomment and execute the below function call statements one by one and observe the output
# display4("Chan",20,12)
# display4("Henry",23)
