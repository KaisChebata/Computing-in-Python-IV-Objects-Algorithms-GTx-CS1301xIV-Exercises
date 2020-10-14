#Write a function called lazy_encrypt. This function should
#take three parameters: two strings and a dictionary. The
#first string is the filename of a file to which to write
#(output_file), the second string is the filename of a file
#from which to read (input_file), and the dictionary is a
#mapping of character:character pairs you should use to
#"encrypt" the contents of the input file before writing it
#to the output file.
#
#lazy_encrypt should go through every character in the
#input file. If the character is a key in the dictionary,
#then lazy_encrypt should write the value associated with
#that key to the output file. If it is not a key, it should
#write the original character.
#
#For example, imagine if the input file contained the text
#"Hello world", and the dictionary was {"e": "o", "o": "a"}.
#Then, lazy_encrypt would write "Holla warld" to the output
#file. Each letter is only substituted once. You should not
#ignore case: if the input file had instead contained the
#text "HELLO WORLD", then nothing should have been changed
#because the keys in the dictionary are lower-case.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.


#Write your function here!

def lazy_encrypt(outfile_path: str, infile_path: str, dictionary: dict) -> None:
    # sol 1:
    with open(infile_path, 'r') as input_file, open(outfile_path, 'w') as out_file:
        file_reader = input_file.read()
        for char in file_reader:
            if char in dictionary:
                out_file.write(dictionary[char])
            else:
                out_file.write(char)
    return

    # sol 2:
    # output_file = open(outfile_path, 'w')
    # input_file = open(infile_path)

    # input_reader = input_file.readlines()

    # for sentence in input_reader:
    #     for char in sentence:
    #         if char in dictionary:
    #             output_file.write(dictionary[char])
    #         else:
    #             output_file.write(char)
    # output_file.close()
    # input_file.close()
    # return
#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, the contents of anOutputFile.txt after running
#will be:
#Horo is a protty simplo mossago ta oncrypt
#Whon it's oncryptod, it will laak difforont

input_file_path = 'CS1301xIV_Test_Coding_Problems\\Raw_Files\\tp09_input_file.txt'
output_file_path = 'CS1301xIV_Test_Coding_Problems\\Raw_Files\\tp09_output_file.txt'
lazy_encrypt(output_file_path, input_file_path, {"e": "o", "o": "a"})
print("Done running! Check anOutputFile.txt for the result.")

# print(lazy_encrypt(output_file_path, input_file_path, {"e": "o", "o": "a"}))

