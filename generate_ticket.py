'''
Write a python program to generate the ticket numbers for specified number of passengers 
traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline: src: dest: number
where

Consider AI as the value for airline
src and dest should be the first three characters of the source and destination cities.
number should be auto-generated starting from 101
The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket numbers.

Sample Input	Expected Output
airline = AI
source = Bangalore
destination = London
no_of_passengers = 10	['AI:Ban:Lon:106', 'AI:Ban:Lon:107',
                       'AI:Ban:Lon:108', 'AI:Ban:Lon:109', 'AI:Ban:Lon:110']
airline = BA
source = Australia
destination = France
no_of_passengers = 2 ['BA:Aus:Fra:101', 'BA:Aus:Fra:102']
'''


# PF-Exer-22

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    if no_of_passengers < 5:
        count = 1
        while no_of_passengers != 0:
            ticket_number_list.append(
                airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(100 + count))
            count += 1
            no_of_passengers += -1
    else:
        for i in range(6, no_of_passengers+1):
            ticket_number_list.append(
                airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(100 + i))

    return ticket_number_list


# Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI", "Bangalore", "London", 10))
