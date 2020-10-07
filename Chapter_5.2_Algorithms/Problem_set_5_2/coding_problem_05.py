# Write a function called search_for_string() that takes two
# parameters, a list of strings, and a string. This function
# should return a list of all the indices at which the
# string is found within the list.
#
# You may assume that you do not need to search inside the
# items in the list; for examples:
#
#  search_for_string(["bob", "burgers", "tina", "bob"], "bob")
#      -> [0,3]
#  search_for_string(["bob", "burgers", "tina", "bob"], "bae")
#      -> []
#  search_for_string(["bob", "bobby", "bob"])
#      -> [0, 2]
#
# Use a linear search algorithm to achieve this. Do not
# use the list method index.
#
# Recall also that one benefit of Python's general leniency
# with types is that algorithms written for integers easily
# work for strings. In writing search_for_string(), make sure
# it will work on integers as well -- we'll test it on
# both.


# Write your code here!

def search_for_string(lst, search_term):
    # indices_lst = []
    # for index in range(len(lst)):
    #     if lst[index] == search_term:
    #         indices_lst.append(index)
    # return indices_lst
    return [index for index in range(len(lst)) if lst[index] == search_term]

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: [1, 4, 5]
def demo(sample_list, search_string):
    print(search_for_string(sample_list, search_string))


demo(["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"], "turnip")
demo(["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"], "tomato")
demo(["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"], "artichoke")
demo([11, 23, 44, 11, 76, 95, 11, 90, -3, 11, 10], 11)