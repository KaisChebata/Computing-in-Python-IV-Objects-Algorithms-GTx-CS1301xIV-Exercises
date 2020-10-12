# For our last data analysis-inspired problem, 
# let's go back to one of my favorite examples: Pokemon. 
# Pokemon is a popular video game franchise by Nintendo which features over 800 monsters, 
# called Pokemon, each with unique names, types, and statistics.

# The dataset you'll have for this problem contains every Pokemon through Generation 7, 
# including their alternate forms. 
# You don't need to understand Pokemon to solve this problem, 
# though: games are just good candidates for this kind of analysis because 
# they often have well-formed, complete datasets.

# To solve these problems, you just need to know a couple things. 
# First, each row of the dataset corresponds to a Pokemon. 
# Each row has 13 columns, in this order:
#    01- Number: The numbered ID of the Pokemon, an integer
#    02- Name: The name of the Pokemon, a string
#    03- Type1: The Pokemon's primary type, a string
#    04- Type2: The Pokemon's secondary type, a string 
#       (this may be blank; you may assume Type1 and Type2 will never be the same)
#    05- HP: The Pokemon's HP statistic, an integer in the range 1 to 255
#    06- Attack: The Pokemon's Attack statistic, an integer in the range 1 to 255
#    07- Defense: The Pokemon's Defense statistic, an integer in the range 1 to 255
#    08- SpecialAtk: The Pokemon's Special Attack statistic, an integer in the range 1 to 255
#    09- SpecialDef: The Pokemon's Special Defense statistic, an integer in the range 1 to 255
#    10- Speed: The Pokemon's Speed statistic, an integer in the range 1 to 255
#    11- Generation: What generation the Pokemon debuted in, an integer in the range 1 to 7
#    12- Legendary: Whether the Pokemon is considered "legendary" or not, either TRUE or FALSE 
#       (for you hardcore fans, we've grouped Legendary and Mythical Pokemon together for simplicity)
#    13- Mega: Whether the Pokemon is "Mega" or not, either TRUE or FALSE

# Use this information to answer the questions below. 
# Note that although you can do this problem without objects, 
# it will probably be much easier if you initially create a Pokemon object with the 13 attributes above, 
# add a method for calculating a total power based on the sum of those six stats 
# (HP, Attack, Defense, SpecialAtk, SpecialDef, and Speed), 
# read the file into a list of instances of that object, and then do your reasoning based on that list.

#The line below will open a file containing information
#about every pokemon through Generation 7:

pokedex = open('../resource/lib/public/pokedex.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#

#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.
