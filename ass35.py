# PF-Assgn-35

# Global variable
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)


def find_more_than_average():
    number_list = []
    sum = 0
    for num in list_of_marks:
        sum += (num * 100 / 25)
        print(sum)
    avg = sum / 10
    print(avg)
    for marks in list_of_marks:
        if ((marks / 25) * 100 > avg):
            number_list.append(marks)
    return number_list


def sort_marks():
    pass


def generate_frequency():
    pass
    # Remove pass and write your logic here


print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
