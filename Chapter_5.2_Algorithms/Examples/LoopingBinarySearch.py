def binary_search(lst, search_term):
    #First, the list must be sorted.
    lst.sort()

    #Now, each iteration of the loop, we'll narrow
    #down the part of the list to look at.
    min_ = 0
    max_ = len(lst) - 1

    # looping as long as our range has any numbers left to investigate.

    while min_ <= max_:
        # check the middle item of the current range
        current_middle = (min_ + max_) // 2

        # If the term in the middle is the term we're looking for, we're done!
        if lst[current_middle] == search_term:
            return True
        
        # If not, we want to check if the term we're looking for should come earlier or later.

        # If the term we're looking for is less than the current middle, 
        # then search the first half of the list:
        elif search_term < lst[current_middle]:
            max_ = current_middle - 1

        # If the term we're looking for is greater than the current middle, 
        # search the second half of the list:
        else:
            min_ = current_middle + 1
    return False 


intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))
print('---------------------------------------------')
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print('Lucy is in strlist:', binary_search(strlist, 'Lucy'))
print('---------------------------------------------')
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]

print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))