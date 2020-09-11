# PF-Tryout

# Program to be tested

def boarding(seat_num):
    if(seat_num >= 1 and seat_num <= 25):
        batch_no = 1
    elif(seat_num >= 26 and seat_num <= 100):
        batch_no = 2
    elif(seat_num >= 101 and seat_num <= 200):
        batch_no = 3
    else:
        batch_no = -1
    return batch_no
