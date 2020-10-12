def check_anagram(data1, data2):
    count = 0
    if ''.join(sorted(data1.lower())) == ''.join(sorted(data2.lower())):
        for i in range(len(data1)):
            if data1[i].lower() != data2[i].lower():
                count += 1
            else:
                return False
        if count == len(data1):
            return True
    else:
        return False



