#Write a function called count_capital_consonants. This
#function should take as input a string, and return as output
#a single integer. The number the function returns should be
#the count of characters from the string that were capital
#consonants. For this problem, consider Y a consonant.
#
#For example:
#
# count_capital_consonants("Georgia Tech") -> 2
# count_capital_consonants("GEORGIA TECH") -> 6
# count_capital_consonants("gEOrgIA tEch") -> 0

CONSONANT_LETTERS = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 
                        'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
#Write your function here!
def count_capital_consonants(string: str) -> int:
    # sol 1:
    consonants_count = 0
    for char in string:
        if char not in 'AEIOU':
            if 'B' < char < 'Z':
                consonants_count += 1
    return consonants_count
    # 
    # sol 2:
    # return len([consonants for consonants in string if consonants in CONSONANT_LETTERS])



    


#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print
#the same output as shown above in the examples.

print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))
