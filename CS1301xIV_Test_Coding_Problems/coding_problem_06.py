#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.


#Write your function here!

def are_anagrams(string1: str, string2: str) -> bool:
    # sol 1:
    string1_dict, string2_dict = {}, {}
    for char in string1.lower().replace(' ', ''):
        string1_dict[char] = string1_dict.get(char, 0) + 1

    for char in string2.lower().replace(' ', ''):
        string2_dict[char] = string2_dict.get(char, 0) + 1

    return string1_dict == string2_dict

    # sol 2:
    # letter_lst = []
    # for char in string1.lower().replace(' ', ''):
    #     letter_lst.append(char)
    
    # for char in string2.lower().replace(' ', ''):
    #     if char not in letter_lst:
    #         return False
    #     letter_lst.remove(char)
    
    # return len(letter_lst) == 0


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.

print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))

a_srt = 'aabbaba'
# d = {char:a_srt.count(char) for char in set(a_srt)}
# print(d)