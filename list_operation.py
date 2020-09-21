mark_list = [78, 90, 90, 95, 83, 95]

mark_pos = mark_list.index(90)
print("1: Index position of mark 90:", mark_pos)

mark_list.append(54)
print("2: After adding new marks:", mark_list)

mark_list.insert(2, 98)
print("3: After inserting 98 at the 2nd index position:", mark_list)

mark_list.pop(1)
print("4: After removing the marks at the 1st index position:", mark_list)

mark_list.remove(95)
print("5: After removing the first occurence of 95 from the list:", mark_list)

mark_list.sort()
print("6: After sorting the marks in the given list:", mark_list)

mark_list.reverse()
print("7: After reversing the marks in the given list:", mark_list)
