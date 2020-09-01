'''
Givenalistofintegervalues.Writeapythonprogramtocheckwhetheritcontainssamenumber in adjacentposition.
Display the count of such adjacent occurrences.
Estimated Time: 30 minutes

Sample Input	Expected Output
[1, 1, 5, 100, -20, -20, 6, 0, 0]	3
[10, 20, 30, 40, 30, 20]	0
[1, 2, 2, 3, 4, 4, 4, 10]	3

'''


def get_count(num_list):
    count = 0

    for index in range(0, len(num_list)-1):
        if (num_list[index] == num_list[index + 1]):
            count += 1

    return count


num_list = [
    [1, 1, 5, 100, -20, -20, 6, 0, 0],
    [10, 20, 30, 40, 30, 20],
    [1, 2, 2, 3, 4, 4, 4, 10]
]

for num in num_list:
    print(get_count(num))
