
#Write a function called linear() that takes two parameters
#- a list of strings and a string. Write this function so
#that it returns the first index at which the string is
#found within the list if the string is found, or False if
#it is not found. You do not need to worry about searching
#for the search string inside the individual strings within
#the list: for example, linear(["bobby", "fred"], "bob")
#should return False, but linear(["bob", "fred"], "bob")
#should return 0.
#
#Use a linear search algorithm (not as scary as it sounds).
#Do not use the list method index -- in this exercise,
#you're actually implementing the way the index method
#works!


#Write your code here!
from typing import Union, List

def linear(lst: List[Union[str, int]], search_term: Union[str, int]) -> Union[int, bool]:
    for index in range(len(lst)):
        if lst[index] == search_term:
            return index
    return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6)) # should return int 3
# more tests

lst1 = [22, 29, 45, 11, 31, 38, 1, 13, 32, 20, 43, 35, 3, 43, 41, 5, 12, 44]
lst2 = [47, 12, 16, 9, 3, 28, 25, 45, 40, 3, 12, 22, 2]
lst3 = ["raj", "slimy", "influenza", "emanate", "info", "solve", "lakh", "amniotic", 
        "Stalin", "thyself", "information", "ovoviviparous", "inexact", "Tektronix", 
        "armada", "oxygen"]
lst4 = ["persecute", "Ehrlich", "Bethesda", "Dar", "alveolus", "sustenance", "folksinger", 
        "turpentine", "throne", "modesty", "inconspicuous", "handwritten", "mead", "Marquette", 
        "qualm", "panoramic"]
lst5 = [27, 23, 43, 48, 48, 28, 15, 42, 25]
lst6 = ["larynges", "healthy", "toxicology", "Cecropia", "craftsmen", "shaky", "dome", "consensus", 
        "Argus", "spur", "earwig", "musk", "allotting", "Metzler", "pig", "exhaustive", "claret", 
        "scourge"]
lst7 = ["humble", "actor", "Quantico", "sufficient", "cutout", "impede", "Schuster", "sever", 
        "flu", "compensatory", "Benares", "kerchief", "forge", "fluster", "Tanzania", "palladia", 
        "ravine", "OConnor"]
lst8 = [29, 6, 30, 6, 35, 27, 9, 24]


print(linear(lst1, 6)) # should return False
print(linear(lst2, 3)) # should return int 4
print(linear(lst3, 'ovoviviparous')) # should return int 11
print(linear(lst4, 'plunge')) # should return False
print(linear(lst5, 37)) # should return False
print(linear(lst6, 'spur')) # should return int 9
print(linear(lst7, 'solidify')) # should return False
print(linear(lst8, 30)) # should return int 2