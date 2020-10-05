def sort_with_bubbles(lst):
    # set swap_occurred to True to guarantee the loop run once.
    swap_occurred = True

    # Run the loop as long as the swap occurred previous time.
    while swap_occurred:
        # start off assuming a swap 
        swap_occurred = False
        for i in range(len(lst) - 1):
            # current, nxt = lst[i], lst[i + 1]
            if lst[i] > lst[i + 1]:
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp

                swap_occurred = True
    return lst

# Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
lst1 = [8, 46, 27, 33, 40, 47, 20, 29, 1, 24]
lst2 = [38, 47, 45, 27, 22]
lst3 = [20, 19, 37, 2, 32, 33]
lst4 = [30, 13, 5, 31, 29, 14, 32, 37, 50, 12, 4, 49]
lst5 = [24, 47, 41, 28, 35, 31, 46, 7, 39, 33, 34, 36]

print(sort_with_bubbles([5, 3, 1, 2, 4]))
# print(sort_with_bubbles([34, 16, 2, 78, 4, 6, 1]))
# print(sort_with_bubbles(lst1))
# print(sort_with_bubbles(lst2))
# print(sort_with_bubbles(lst3))
# print(sort_with_bubbles(lst4))
# print(sort_with_bubbles(lst5))


