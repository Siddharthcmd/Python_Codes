def boarding1(seat_number):
    if(seat_number >= 1 and seat_number <= 25):
        batch = 1
    elif(seat_number >= 26 and seat_number <= 100):
        batch = 2
    elif(seat_number >= 101 and seat_number <= 200):
        batch = 3
    else:
        batch = -1
    return batch
