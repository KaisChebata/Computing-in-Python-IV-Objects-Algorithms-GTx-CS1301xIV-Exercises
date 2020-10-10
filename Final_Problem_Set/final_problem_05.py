# A common problem in academic settings is plagiarism
# detection. Fortunately, software can make this pretty easy!
# 
# In this problem, you'll be given two files with text in
# them. Write a function called check_plagiarism with two
# parameters, each representing a filename. The function
# should find if there are any instances of 5 or more
# consecutive words appearing in both files. If there are,
# return the longest such string of words (in terms of number
# of words, not length of the string). If there are not,
# return the boolean False.
# 
# For simplicity, the files will be lower-case text and spaces
# only: there will be no punctuation, upper-case text, or
# line breaks.
# 
# We've given you three files to experiment with. file_1.txt
# and file_2.txt share a series of 5 words: we would expect
# check_plagiarism("file_1.txt", "file_2.txt") to return the
# string "if i go crazy then". file_1.txt and file_3.txt
# share two series of 5 words, and one series of 11 words:
# we would expect check_plagiarism("file_1.txt", "file_3.txt")
# to return the string "i left my body lying somewhere in the
# sands of time". file_2.txt and file_3.txt do not share any
# text, so we would expect check_plagiarism("file_2.txt",
# "file_3.txt") to return the boolean False.
# 
# Be careful: there are a lot of ways to do this problem, but
# some would be massively time- or memory-intensive. If you
# get a MemoryError, it means that your solution requires
# storing too much in memory for the code to ever run to
# completion. If you get a message that says "KILLED", it
# means your solution takes too long to run.


# Add your code here!

def check_plagiarism(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        f1_content = f1.read().split(' ')
        f2_content = f2.read().split(' ')
    
    longest_consecutive = []

    for i in range(len(f1_content)):
        for j in range(len(f2_content)):
            current_consecutive_words = []

            if f1_content[i] == f2_content[j]:
                current_i_index = i
                current_j_index = j
                
                while f1_content[current_i_index] == f2_content[current_j_index]:
                    current_consecutive_words.append(f1_content[current_i_index])
                    if current_i_index < len(f1_content) - 1 and current_j_index < len(f2_content) - 1:
                        current_i_index += 1
                        current_j_index += 1
                    else:
                        break
            if len(current_consecutive_words) > len(longest_consecutive):
                longest_consecutive = current_consecutive_words
    
    if len(longest_consecutive) >= 5:
        return ' '.join(longest_consecutive)
    else:
        return False

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
# 
# If your function works correctly, this will originally
# print:
# if i go crazy then
# i left my body lying somewhere in the sands of time
# False
print(check_plagiarism("Final_Problem_Set\\file_1.txt", "Final_Problem_Set\\file_2.txt"))
print(check_plagiarism("Final_Problem_Set\\file_1.txt", "Final_Problem_Set\\file_3.txt"))
print(check_plagiarism("Final_Problem_Set\\file_2.txt", "Final_Problem_Set\\file_3.txt"))
# ------------------------------------------------------------