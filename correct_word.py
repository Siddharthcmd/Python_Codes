# PF-Assgn-48

def find_correct(word_dict):
    count_list = []
    correct = almost_correct = wrong = 0
    for key, value in word_dict.items():
        count = 0
        if (key == value):
            correct += 1
        elif (len(key) == len(value)):
            for i in range(0, len(key)):
                if (key[i] != value[i]):
                    count += 1
            if (count <= 2):
                almost_correct += 1
            else:
                wrong += 1
        else:
            wrong += 1
    count_list.append(correct)
    count_list.append(almost_correct)
    count_list.append(wrong)

    return count_list


word_dict = {"THEIR": "THEIR",  "BUSINESS": "BISINESS",
             "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))
