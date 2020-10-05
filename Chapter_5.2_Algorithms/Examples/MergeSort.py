def mergesort(lst):
    if len(lst) <= 1:
        return lst
    else:
        midpoint = len(lst) // 2
        left = mergesort(lst[:midpoint])
        right = mergesort(lst[midpoint:])

        sorted_lst = []
        while len(left) and len(right) > 0:
            if left[0] < right[0]:
                sorted_lst.append(left[0])
                del left[0]
            else:
                sorted_lst.append(right[0])
                del right[0]
        sorted_lst.extend(left)
        sorted_lst.extend(right)
    return sorted_lst

#Let's try it out!

lst1 = [5, 3, 1, 2, 4]
lst2 = [21, 7, 38, 23, 18, 19, 47, 35]
lst3 = [7, 12, 9, 29, 36, 43, 30, 39, 20, 47]
lst4 = [28, 10, 19, 26, 5, 1, 48, 8, 40, 39, 6, 33]
lst5 = [9, 1, 6, 19, 21, 12, 35]
lst6 = [44, 8, 33, 37, 4, 6]
print(mergesort(lst1))
print(mergesort(lst2))
print(mergesort(lst3))
print(mergesort(lst4))
print(mergesort(lst5))

