'''
Given a string containing uppercase characters(A-Z), compress the string using
Run Length encoding. Repetition of character has to be replaced by storing the
length of that run.

Write a python function which performs the run length encoding for a given
String and returns the run length encoded String.

Provide different String values and test your program.

Sample Input	Expected Output
AAAABBBBCCCCCCCC	4A4B8C
AABCCA	2A1B2C1A
'''

from collections import OrderedDict


def runLengthEncoding(input):

    dict = OrderedDict.fromkeys(input, 0)
    print(dict)
    for ch in input:
        print(dict[ch])
        dict[ch] += 1
    print(dict)
    output = ''
    for key, value in dict.items():
        output = output + key + str(value)
    return output


def encode(message):
    i = 0
    encoded_message = ""
    while (i < len(message)):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message) - 1):
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + str(count) + ch
        i = j+1
    return encoded_message


print(encode("BBBBCCCfffffCCCCfffffCATtttt"))
print(runLengthEncoding("BBBBCCCffffBBBBBfCCCCfffffCATtttt"))
