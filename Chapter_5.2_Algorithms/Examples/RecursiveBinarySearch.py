def binary_search(lst, search_term):
    # First we sort the list
    lst.sort()

    # With each recursive call to binary_search, the size
    # of the list will be cut in half, rounding down. If
    # the search term is not found, then eventually an
    # empty list will be passed into binary_search. So,
    # if searchList is empty, we know that the search
    # term was not found, and we can return False. This
    # is the base case for the recursive binary_search.

    if len(lst) == 0:
        return False
    
    # If there are still items in the list, then we want
    # to find if searchTerm is greater than, less than,
    # or equal to the middle term in the list. For that,
    # we need the index of the middle term.

    middle = len(lst) // 2 

    # First, the easy case: if it's the middle term, we found it! Return True.
    if search_term == lst[middle]:
        return True
    
    # If the search term is less than the middle term,
    # then repeat the search on the left half of the list.
    elif search_term < lst[middle]:
        return binary_search(lst[:middle], search_term)
    
    # If the search term is greater than the middle 
    # term, then repeat the search on the right half of the list.
    else:
        return binary_search(lst[middle + 1 :], search_term)

intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

print('---------------------------------------------')

strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

print('---------------------------------------------')
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))

    