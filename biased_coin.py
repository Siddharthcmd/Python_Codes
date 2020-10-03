import random


def biasedflip():

    global TotalTails
    global TotalHeads

    if random.randint(1, 100) < Probability:

        print("head")
        TotalHeads += 1

    else:

        print("tails")
        TotalTails += 1


TotalHeads = 0
TotalTails = 0
i = 0
Probability = 70
NumberOfTrials = 100


while i < NumberOfTrials:
    biasedflip()
    i += 1

print("After {0} flips there was {1} Head(s) and {2} Tail(s)".format(
    NumberOfTrials, TotalHeads, TotalTails))
