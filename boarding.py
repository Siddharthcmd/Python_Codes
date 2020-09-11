def boarding1(seat_num):
    if(seat_num >= 1 and seat_num <= 25):
        batch = 1
    elif(seat_num >= 26 and seat_num <= 100):
        batch = 2
    elif(seat_num >= 101 and seat_num <= 200):
        batch = 3
    else:
        batch = -1
    return batch
