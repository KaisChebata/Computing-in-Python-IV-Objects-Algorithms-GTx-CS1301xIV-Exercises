#Write a function called rabbit_hole. rabbit_hole should have
#two parameters: a dictionary and a string. The string may be
#a key to the dictionary. The value associated with that key,
#in turn, may be another key to the dictionary.
#
#Keep looking up the keys until you reach a key that has no
#associated value. Then, return that key.
#
#For example, imagine if you had the following dictionary.
#This one is sorted to make this example easier to follow:
#
# d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
#      "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
#      "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
#      "rat": "ram", "ram": "rat"}
#
#If we called rabbit_hole(d, "bat"), then our code should...
#
# - Look up "bat", and find "pig"
# - Look up "pig", and find "cat"
# - Look up "cat", and find "dog"
# - Look up "dog", and find "ant"
# - Look up "ant", and find no associated value, and so it would
#   return "ant".
#
#Other possible results are:
#
# rabbit_hole(d, "bat") -> "fly"
# rabbit_hole(d, "ewe") -> "hen"
# rabbit_hole(d, "jay") -> "doe"
# rabbit_hole(d, "yak") -> "yak"
#
#Notice that if the initial string passed in is not a key in
#the dictionary, that string should be returned as the result as
#well.
#
#Note, however, that it is possible to get into a loop. In the
#dictionary above, rabbit_hole(d, "rat") would infinitely go
#around between "rat" and "ram". You should prevent this: if a
#key is ever accessed more than once (meaning a loop has been
#reached), return the boolean False.
#
#Hint: If you try to access a value from a dictionary that does
#not exist, a KeyError will be raised.

#Write your function here!
from typing import Union
def rabbit_hole(dictionary: dict, key: str) -> Union[str, bool]:
    try:
        if key not in dictionary:
            return key
        else:
            return rabbit_hole(dictionary, dictionary.get(key))
    except:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ant, hen, doe, yak, False, each on their own line.
d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))

# test cases:

dict1 = {'James': 'eastward', 'TOEFL': 'James', 'eastward': 'Billiken', 'argument': 'Billiken', 
         'bulkhead': 'eastward', 'Sci': 'bulkhead'}

dict2 = {'pig': 'guy', 'ultimate': 'pig', 'sawtimber': 'bosonic', 'gland': 'landlord', 'weed': 'guy'}

dict3 = {'footwear': 'seventyfold', 'satiety': 'quid', 'compartment': 'gratuitous', 
         'curtain': 'classify', 'Anabaptist': 'seventyfold', 'went': 'classify', 
         'pat': 'intensive', 'glutamine': 'seventyfold', 'admitted': 'footwear', 
         'seventyfold': 'curtain', 'toady': 'satiety'}

dict4 = {'footwear': 'seventyfold', 'satiety': 'quid', 'compartment': 'gratuitous', 
         'curtain': 'classify', 'Anabaptist': 'seventyfold', 'went': 'classify', 'pat': 'intensive', 
         'glutamine': 'seventyfold', 'admitted': 'footwear', 'seventyfold': 'curtain', 
         'toady': 'satiety'}

dict5 = {'footwear': 'seventyfold', 'satiety': 'quid', 'compartment': 'gratuitous', 
         'curtain': 'classify', 'Anabaptist': 'seventyfold', 'went': 'classify', 'pat': 'intensive', 
         'glutamine': 'seventyfold', 'admitted': 'footwear', 'seventyfold': 'curtain', 
         'toady': 'satiety'}

# case 1:
# with dict1 given and initial_key = "Sci". We expected rabbit_hole to return the str "Billiken"

# case 2:
# with dict1 given and initial_key = "TOEFL". We expected rabbit_hole to return the str "Billiken"

# case 3:
# with dict1 given and initial_key = "eastward". We expected rabbit_hole to return the str "Billiken"

# case 4:
# with dict2 given and initial_key = "gland". We expected rabbit_hole to return the str "landlord"

# case 5:
# with dict2 initial_key = "landlord". We expected rabbit_hole to return the str "landlord"

# case 6:
# with dict3 given and initial_key = "satiety". We expected rabbit_hole to return the str "quid"

# case 7:
# with dict4 given and initial_key = "glutamine". We expected rabbit_hole to return the str "classify"

# case 8:
# with dict5 given and initial_key = "curtain". We expected rabbit_hole to return the str "classify"
