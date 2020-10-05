def sort_with_select(a_list):
    # for each index in the list
    for i in range(len(a_list)):
        # Assume first that current item is in the correct order ...
        min_index = i

        # for each item from i to the end of the list
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        
        min_value = a_list[min_index] # save current minimum value
    
        del a_list[min_index] # delete the minimum value from the current index.
        a_list.insert(i, min_value) # insert the minmum value at its new index.
        
    return a_list


lst1 = [5, 3, 1, 2, 4]
lst2 = [21, 7, 38, 23, 18, 19, 47, 35]
lst3 = [7, 12, 9, 29, 36, 43, 30, 39, 20, 47]
lst4 = [28, 10, 19, 26, 5, 1, 48, 8, 40, 39, 6, 33]
lst5 = [9, 1, 6, 19, 21, 12, 35]
lst6 = [44, 8, 33, 37, 4, 6]

print(sort_with_select(lst1))
print(sort_with_select(lst2))
print(sort_with_select(lst3))
print(sort_with_select(lst4))
print(sort_with_select(lst5))
print(sort_with_select(lst6))