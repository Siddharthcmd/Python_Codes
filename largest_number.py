
def create_largest_number(number_list):
    str_num = ""
    for num in number_list:
        for i in str(num):
            str_num += i
    return "".join(sorted(str_num, reverse=True))


number_list = [23, 34, 55]
largest_number = create_largest_number(number_list)
print(largest_number)
