# PF-Assgn-50

def sms_encoding(data):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    word = data.split()
    ab_list = []

    for i in range(0, len(word)):
        if (len(word[i]) == 1):
            ab_list.append(word[i])
        else:
            for j in word[i]:
                if j in vowel_list:
                    word[i] = word[i].replace(j, "")
            ab_list.append(word[i])

    return " ".join(ab_list)


data = "MSD says I love cricket and tennis too"
print(sms_encoding(data))
