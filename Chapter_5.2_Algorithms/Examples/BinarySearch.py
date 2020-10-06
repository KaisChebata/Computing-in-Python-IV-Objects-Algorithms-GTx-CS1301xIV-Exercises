def looping_binary_search(lst, search_term):
    lst.sort()
    min_ = 0
    max_ = len(lst) - 1

    while min_ <= max_:
        current_middle = (min_ + max_) // 2
        if lst[current_middle] == search_term:
            return True
        elif search_term < lst[current_middle]:
            max_ = current_middle - 1
        else:
            min_ = current_middle + 1
    return False

def recursive_binary_search(lst, search_term):
    lst.sort()
    
    if len(lst) == 0:
        return False

    middle = len(lst) // 2
    if lst[middle] == search_term:
        return True
    elif search_term < lst[middle]:
        return recursive_binary_search(lst[:middle], search_term)
    else:
        return recursive_binary_search(lst[middle + 1:], search_term)

intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist (looping):", looping_binary_search(intlist, 23))
print("50 is in intlist (looping):", looping_binary_search(intlist, 50))
print("23 is in intlist (recursive):", recursive_binary_search(intlist, 23))
print("50 is in intlist (recursive):", recursive_binary_search(intlist, 50))