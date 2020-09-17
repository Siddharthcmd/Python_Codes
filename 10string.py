# PF-Assgn-41
def find_ten_substring(num_str):
    # list to store the sub-string
    ten_substr = []
    # itiritar from the starting of the string to end of the string
    for i in range(len(num_str)):
        # string to save the sub_string whoes value is 10
        sub_str = ""
        # variable to store sum
        sum = 0
        # loop to itritate thru the string and calculate the sum
        for j in range(i, len(num_str)):
            sum += int(num_str[j])
            # condition to check weather the sum is les than 10 or equal to 10
            # if sum is less than 10 store the value in sub string
            if (sum < 10):
                sub_str += num_str[j]
            # if sum is equal to 10 append the value into the list
            elif (sum == 10):
                sub_str += num_str[j]
                ten_substr.append(sub_str)
                # check if my current index is not my last index to avoid out of bound error
                if (j != len(num_str) - 1):
                    # check if the next value of index is zero if true it does not make sum as zero
                    # and countinue with next itration else break
                    if (num_str[j + 1] == "0"):
                        continue
                    else:
                        break
    print(ten_substr)


num_str = "153512350121245315212"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)
