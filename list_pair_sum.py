'''
Write a python function, find_pairs_of_numbers() which accepts a list 
of positive integers with no repetitions and returns count of pairs of 
numbers in the list that adds up to n. The function should return 0, 
if no such pairs are found in the list.

Also write the pytest test cases to test the program.

Sample Input	Expected Output
[1, 2, 7, 4, 5, 6, 0, 3], 6	3
[3, 4, 1, 8, 5, 9, 0, 6], 9	4
'''
# PF-Assgn-34


def find_pairs_of_numbers(num_list, n):
    count = 0
    for i in range(0, len(num_list)):
        for j in range(i + 1, len(num_list)):
            if (num_list[i] + num_list[j] == n):
                count += 1
    return count


num_list = [3, 4, 1, 8, 5, 9, 0, 6]
n = 9
print(find_pairs_of_numbers(num_list, n))
